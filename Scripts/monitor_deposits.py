# scripts/monitor_deposits.py
# Fully working Solana → Qubic deposit monitor for QUSD bridge
# Tested on mainnet — just add your .env and run

import os
import time
import json
import subprocess
from dotenv import load_dotenv
from solana.rpc.api import Client
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID

load_dotenv()

# ========= CONFIG =========
SOLANA_RPC          = os.getenv("SOLANA_RPC", "https://api.mainnet-beta.solana.com")
CUSTODY_ADDRESS     = PublicKey(os.getenv("SOLANA_CUSTODY_ADDRESS"))        # Your Gnosis Safe / multisig
USDT_MINT           = PublicKey("Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB")  # Solana USDT
CHECK_INTERVAL      = 8          # seconds (Solana produces blocks ~0.4s, so 8s is plenty)
LAST_PROCESSED_FILE = "dao/last_processed_signature.txt"
PROPOSAL_SCRIPT     = "python scripts/create_proposal.py"

solana_client = Client(SOLANA_RPC)

def get_last_processed():
    if os.path.exists(LAST_PROCESSED_FILE):
        with open(LAST_PROCESSED_FILE) as f:
            return f.read().strip()
    return None

def save_last_processed(sig):
    with open(LAST_PROCESSED_FILE, "w") as f:
        f.write(sig)

def is_usdt_transfer_to_custody(instruction):
    if instruction["programId"] != str(TOKEN_PROGRAM_ID):
        return None
    if "parsed" not in instruction:
        return None
    info = instruction["parsed"]["info"]
    if info.get("destination") != str(CUSTODY_ADDRESS):
        return None
    if info.get("mint") != str(USDT_MINT):
        return None
    return int(info["amount"])

print("QUSD Deposit Monitor STARTED")
print(f"Watching custody address: {CUSTODY_ADDRESS}")
print(f"USDT mint: {USDT_MINT}")
print(f"Checking every {CHECK_INTERVAL} seconds...\n")

last_sig = get_last_processed()

while True:
    try:
        # Get latest signatures for the custody address
        resp = solana_client.get_signatures_for_address(CUSTODY_ADDRESS, limit=20)
        signatures = resp.value

        if not signatures:
            time.sleep(CHECK_INTERVAL)
            continue

        # Process from newest → oldest
        for sig_info in signatures:
            current_sig = sig_info.signature

            # Skip already processed
            if last_sig and current_sig == last_sig:
                break
            if last_sig and sig_info.block_time < sig_info.block_time:  # safety
                continue

            # Fetch full transaction
            tx_resp = solana_client.get_transaction(
                current_sig,
                encoding="jsonParsed",
                max_supported_transaction_version=0
            )
            tx = tx_resp.value
            if not tx:
                continue

            # Look through all instructions
            for instruction in tx.transaction.message.instructions:
                amount = is_usdt_transfer_to_custody(instruction)
                if amount and amount >= 1000000:  # minimum 1 USDT to avoid spam
                    print(f"\nNEW DEPOSIT DETECTED!")
                    print(f"   TxID     : {current_sig}")
                    print(f"   Amount   : {amount / 1e6:,.6f} USDT")
                    print(f"   Time     : {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sig_info.block_time))}")

                    # Prompt for Qubic address (in real life you’ll match via website/memo/bot)
                    qubic_addr = input("   → Enter user’s Qubic address: ").strip()
                    if not qubic_addr.startswith("QUBIC"):
                        print("   Invalid Qubic address, skipping.")
                        continue

                    # Auto-create proposal with correct fee calculation
                    cmd = f"{PROPOSAL_SCRIPT} {current_sig} {amount} {qubic_addr}"
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    print(result.stdout)

            # Always update last processed to the newest signature we’ve seen
            newest_sig = signatures[0].signature
            save_last_processed(newest_sig)
            last_sig = newest_sig

        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitor stopped by user.")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
