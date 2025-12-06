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

A transparent, DAO-governed bridge that brings USDT from Solana to Qubic as fully backed QUSD.

## Fee Structure (as of December 2025 – governed by on-chain proposals)

| Action                     | Fee                          | Who receives it                          | Notes                                                                 |
|----------------------------|------------------------------|------------------------------------------|-----------------------------------------------------------------------|
| Deposit (USDT → QUSD)      | **0.15%**                    | 100% to DAO treasury                     | Covers operational costs, audits, security, and future development    |
| Redemption (QUSD → USDT)   | **0.20%**                    | 100% to DAO treasury                     | Slightly higher to discourage rapid in/out during volatile periods   |
| No fee on transfers        | 0%                           | —                                        | QUSD transfers inside Qubic remain completely free                     |
| Emergency withdrawal fee   | 1% (only if activated)       | DAO treasury + liquidity buffer          | Only activatable by 70% DAO supermajority in case of critical threat  |

### Example
- You deposit 10,000 USDT → pay 15 USDT fee → receive **9,985 QUSD**
- You later redeem 9,985 QUSD → pay 19.97 USDT fee → receive **9,965.03 USDT** back

### How fees are used (transparent treasury)
All collected fees go to a public, on-chain DAO treasury and are allocated as follows (current governance rule):

| Purpose                        | Percentage |
|-------------------------------|------------|
| Third-party audits & security | 40%        |
| Multisig signer compensation & insurance | 25%        |
| Development & tooling         | 20%        |
| Liquidity incentives & marketing | 10%        |
| Community grants & bug bounties | 5%         |

Treasury address and real-time spending dashboard: https://explorer.qubic.org/address/dao-treasury-xxxx (will be published at launch)

Fees can be changed at any time via on-chain DAO proposal (requires 60% approval + 14-day voting period).

---

Everything else in the README remains the same as the previous version.
Just replace or append this fee section wherever you prefer (usually right after “How It Works” or before “Getting Started”).

Let me know if you want a zero-fee launch period, tiered fees, or referral discounts added!
