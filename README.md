# QUSD – USDT → Qubic 1:1 Backed Stablecoin (Hybrid DAO Bridge)

A human-governed, transparent, and auditable bridge that brings USDT liquidity from Solana to the Qubic network as QUSD, without relying on centralized exchanges or fully automated bridge protocols.

## How It Works – Hybrid DAO Model

The system is intentionally hybrid: it combines decentralized governance with clearly defined points of centralized execution to maximize security, transparency, and auditability.

### 1. Centralized Asset Custody (The Trust Point)
- A multi-signature wallet (or Gnosis-style Safe) on **Solana** receives the user’s USDT.
- Keys are distributed among trusted DAO members (different individuals/geographies).
- This custody step is the only centralized point of trust, but it is governed by the DAO.

### 2. Decentralized Decision Making
- The DAO consists of **100+ agents/members** running on the Qubic network (Qubic-based DAO).
- Every incoming USDT deposit is verified on-chain by the DAO members.
- A **supermajority vote (e.g., ≥51% or higher threshold)** is required to confirm that the correct amount of USDT has been received.

### 3. Centralized Minting Action
- Once DAO consensus is reached, an **authorized executor** (one of the multisig signers or a permissioned role) triggers the QUSD minting function on Qubic.
- A permissioned smart contract on Qubic mints **exactly the same amount** of QUSD directly into the user’s Qubic wallet.

### 4. Auditing & Transparency
- The DAO commits to publishing **regular third-party audits** (at least quarterly or after significant volume milestones).
- Audits must prove 1:1 backing: every QUSD in circulation = USDT held in the Solana custody wallet.
- On-chain proof of reserves and public dashboard (in development) will be available for real-time verification.

## Summary Table

| Question                              | Answer                                                                                 |
|---------------------------------------|----------------------------------------------------------------------------------------|
| Do you replace a third-party CEX?     | Yes – the DAO becomes the new trusted counterparty instead of Binance, Coinbase, etc. |
| Do you replace an automated bridge?   | Yes – DAO consensus replaces oracles and bridge validator sets.                        |
| Are you fully decentralized?          | No – custody of USDT on Solana remains a managed multisig (centralized point of trust).|
| Where is the trust placed?            | In the DAO members and the transparency/audit process instead of a single corporation.|

This model deliberately moves trust from a single company or fully trustless (but complex) bridge protocol to a large, identifiable group of individuals governed by on-chain voting and regular independent audits.

## Getting Started (User Flow)

1. User sends USDT to the official Solana custody address (published and verified by the DAO).
2. User submits their Qubic address together with the Solana txid (via website / bot / dashboard).
3. DAO members detect and verify the deposit.
4. Automated proposal → DAO vote → supermajority approval.
5. Authorized executor mints QUSD 1:1 to the user’s Qubic wallet.
6. Transaction complete – user now holds fully backed QUSD on Qubic.

## Repository Contents (planned / in progress)

- `/contracts` – Permissioned QUSD minter smart contract for Qubic
- `/scripts`   – Deposit monitoring & proposal automation tools
- `/audits`     – Published third-party audit reports
- `/dao`        – Governance contracts / member list / voting records
- `/frontend`   – User deposit portal & proof-of-reserves dashboard

## Links

- Website: (coming soon)
- DAO governance portal: (coming soon)
- Solana custody address: (to be announced after multisig deployment)
- Latest audit: (to be published)

We are building in public – feedback and new DAO members are welcome.

Made with transparency by the QUSD DAO

# QUSD – USDT → Qubic 1:1 Backed Stablecoin (Hybrid DAO Bridge)

A human-governed, transparent, and auditable bridge that brings USDT liquidity from Solana to the Qubic network as QUSD, without relying on centralized exchanges or fully automated bridge protocols.

## How It Works – Hybrid DAO Model

The system is intentionally hybrid: it combines decentralized governance with clearly defined points of centralized execution to maximize security, transparency, and auditability.

### 1. Centralized Asset Custody (The Trust Point)
- A multi-signature wallet (or Gnosis-style Safe) on **Solana** receives the user’s USDT.
- Keys are distributed among trusted DAO members (different individuals/geographies).
- This custody step is the only centralized point of trust, but it is governed by the DAO.

### 2. Decentralized Decision Making
- The DAO consists of **100+ agents/members** running on the Qubic network (Qubic-based DAO).
- Every incoming USDT deposit is verified on-chain by the DAO members.
- A **supermajority vote (e.g., ≥51% or higher threshold)** is required to confirm that the correct amount of USDT has been received.

### 3. Centralized Minting Action
- Once DAO consensus is reached, an **authorized executor** (one of the multisig signers or a permissioned role) triggers the QUSD minting function on Qubic.
- A permissioned smart contract on Qubic mints **exactly the same amount** of QUSD directly into the user’s Qubic wallet.

### 4. Auditing & Transparency
- The DAO commits to publishing **regular third-party audits** (at least quarterly or after significant volume milestones).
- Audits must prove 1:1 backing: every QUSD in circulation = USDT held in the Solana custody wallet.
- On-chain proof of reserves and public dashboard (in development) will be available for real-time verification.

## Summary Table

| Question                              | Answer                                                                                 |
|---------------------------------------|----------------------------------------------------------------------------------------|
| Do you replace a third-party CEX?     | Yes – the DAO becomes the new trusted counterparty instead of Binance, Coinbase, etc. |
| Do you replace an automated bridge?   | Yes – DAO consensus replaces oracles and bridge validator sets.                        |
| Are you fully decentralized?          | No – custody of USDT on Solana remains a managed multisig (centralized point of trust).|
| Where is the trust placed?            | In the DAO members and the transparency/audit process instead of a single corporation.|

This model deliberately moves trust from a single company or fully trustless (but complex) bridge protocol to a large, identifiable group of individuals governed by on-chain voting and regular independent audits.

## Getting Started (User Flow)

1. User sends USDT to the official Solana custody address (published and verified by the DAO).
2. User submits their Qubic address together with the Solana txid (via website / bot / dashboard).
3. DAO members detect and verify the deposit.
4. Automated proposal → DAO vote → supermajority approval.
5. Authorized executor mints QUSD 1:1 to the user’s Qubic wallet.
6. Transaction complete – user now holds fully backed QUSD on Qubic.

## Repository Contents (planned / in progress)

- `/contracts` – Permissioned QUSD minter smart contract for Qubic
- `/scripts`   – Deposit monitoring & proposal automation tools
- `/audits`     – Published third-party audit reports
- `/dao`        – Governance contracts / member list / voting records
- `/frontend`   – User deposit portal & proof-of-reserves dashboard

## Links

- Website: (coming soon)
- DAO governance portal: (coming soon)
- Solana custody address: (to be announced after multisig deployment)
- Latest audit: (to be published)

We are building in public – feedback and new DAO members are welcome.

Made with transparency by the QUSD DAO
