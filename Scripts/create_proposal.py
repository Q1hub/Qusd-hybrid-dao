# scripts/create_proposal.py
import json, sys, time, os

txid = sys.argv[1]
raw_usdt = int(sys.argv[2])           # e.g. 10000000 for 10,000.00 USDT
qubic_addr = sys.argv[3]

fee = int(raw_usdt * 0.0015)          # 0.15%
qusd_amount = raw_usdt - fee

proposal = {
    "proposalId": f"solana-{txid[:12]}-{int(time.time())}",
    "type": "MINT_QUSD",
    "status": "pending",
    "createdAt": int(time.time()),
    "solanaTxId": txid,
    "amountUsdtRaw": str(raw_usdt),
    "amountQusdAfterFee": str(qusd_amount),
    "feeUsdt": str(fee),
    "qubicDestination": qubic_addr,
    "yesVotes": 0,
    "noVotes": 0,
    "requiredSupermajority": 67
}

os.makedirs("dao/proposals/pending", exist_ok=True)
path = f"dao/proposals/pending/{txid[:32]}.json"
with open(path, "w") as f:
    json.dump(proposal, f, indent=2)

print(f"Proposal created → {qusd_amount / 1e6} QUSD for {qubic_addr}")
