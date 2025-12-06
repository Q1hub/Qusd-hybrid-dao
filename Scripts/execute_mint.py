# scripts/execute_mint.py
import sys, json, os
from pyqubic import QubicClient  # replace with real SDK when ready

client = QubicClient(private_key=os.getenv("EXECUTOR_KEY"))
contract_id = os.getenv("QUSD_CONTRACT_ID")

proposal_file = sys.argv[1]
with open(proposal_file) as f:
    p = json.load(f)

amount = int(p["amountQusdAfterFee"])
to_addr = p["qubicDestination"]

tx = client.call_contract(contract_id, "mint", [to_addr, amount])
print(f"MINTED {amount/1e6} QUSD → {to_addr} | TX {tx}")
