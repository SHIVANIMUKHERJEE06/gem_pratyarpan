# 🏛️ GeM Pratyarpan (प्रत्यार्पण)
> **National Consignee Reverse Logistics, Inspection Dispute & Multi-Ledger Refund Reconciliation Engine**  
> *Developed for IMPACTX 2026 — Problem Statement 15: "The Return That Shouldn't Be a Hassle"*

[![Frontend Deployment](https://img.shields.io/badge/Vercel-Live%20Portal-000000?style=for-the-badge&logo=vercel)](https://gempratyarpan-frontend.vercel.app)
[![Backend API](https://img.shields.io/badge/Render-API%20Active-46E3B7?style=for-the-badge&logo=render)](https://gem-pratyarpan.onrender.com/api/health)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Tests: 15/15 Passed](https://img.shields.io/badge/Test%20Harness-15%2F15%20Passed-brightgreen?style=for-the-badge)](verification_harness.py)

---

## 🌐 Live Deployments & Quick Links
* 🚀 **Live Production Frontend (Vercel):** [https://gempratyarpan-frontend.vercel.app](https://gempratyarpan-frontend.vercel.app)
* ⚙️ **Production API Gateway (Render):** [https://gem-pratyarpan.onrender.com](https://gem-pratyarpan.onrender.com)
* 🩺 **Backend Health Endpoint:** [https://gem-pratyarpan.onrender.com/api/health](https://gem-pratyarpan.onrender.com/api/health)
* 📦 **GitHub Repository:** [https://github.com/SHIVANIMUKHERJEE06/gem_pratyarpan](https://github.com/SHIVANIMUKHERJEE06/gem_pratyarpan)

---

## 📌 Executive Summary & The Problem

On public procurement platforms such as the **Government e-Marketplace (GeM)**, purchase orders aggregate high volumes of distinct line items across diverse vendors. Payments are funded through multi-split public budgets combining Central PFMS Treasury Grants, Department Wallet Balances, and Promotional Subsidies.

### The Real-World Breakdown in Legacy Portals
1. **Monolithic Order-Level Rejections:** When a single consignee item arrives damaged or fails inspection, existing workflows freeze the entire multi-vendor purchase order, delaying payments for compliant sellers.
2. **Asynchronous Ledger Latency & Black Holes:** The GeM platform, the Payment Gateway, and the Public Financial Management System (PFMS) operate on disconnected ledgers. An item marked "Refund Initiated" often remains locked in settlement reconciliation limbo for months.
3. **Subjective "He-Said-She-Said" Logistics:** Logistics providers often register false delivery attempts ("Buyer premises closed") to evade SLA penalties, while consignees lack an objective dispute resolution mechanism.
4. **Disproportionate Risk Scoring:** High-volume government research facilities (e.g., pathology labs returning temperature-sensitive reagents) get erroneously penalized by crude anti-abuse algorithms without an appeal route.

---

## 💡 What Sets GeM Pratyarpan Apart?

Instead of presenting a static dashboard, **GeM Pratyarpan** operates as an **Autonomous Item-Level Settlement & Reverse Logistics State Engine**:

* ⚡ **Decoupled Item Micro-Lifecycles:** Line items move through discrete, independent state transitions (`REQUESTED` ➔ `COLLECTION_PENDING` ➔ `INSPECTION_DISPUTE` ➔ `REFUND_INITIATED` ➔ `CREDIT_DISBURSED`) without freezing companion goods.
* 🔄 **Three-Way Asynchronous Ledger Reconciliation:** Cross-references the **Seller Portal**, **Payment Gateway**, and **PFMS Treasury Ledger** in real time, auto-classifying records into **Waiting** (<48h SLA) vs. **Stuck** (>48h SLA with auto-escalation).
* 🛡️ **Cryptographic Idempotency Guard (`X-Idempotency-Key`):** Enforces transaction deduplication at the protocol level. Live re-clicks, timeout retries, or duplicate webhook payloads can never trigger secondary debits from public accounts.
* 💸 **Proportional Multi-Instrument Refund Waterfall:** Mathematically deconstructs gross refund amounts across Treasury grants, department wallets, and subsidy pools down to the exact paisa.
* ⚖️ **Objective Quality & Logistics Arbitration Desk:** Implements side-by-side evidence analysis (e.g., Consignee damage photos vs. Seller tamper-proof dispatch seals) with SLA clocks and transparent administrative outcomes.
* 📜 **Append-Only Tamper-Evident SHA-256 Ledger:** Logs every actor, event, state transition, and arbitration decision into an immutable audit trail.
## 🧭 Application Modules & User Workflow
---
### 1. 📦 Item-Level Consignments (`#orders-tab`)
* Review purchase orders partitioned by individual line items.
* Click **"⚙️ Waterfall"** on any item to view its proportional refund split across treasury, wallet, and subsidy pools.
* Click **"⚡ Disburse Refund"** to execute the waterfall.
* *Idempotency Stress Test:* Click "Disburse Refund" a second time; the system intercepts duplicate execution and triggers the Idempotency Replay Guard.

### 2. ⚖️ Inspection & Logistics Arbitration Desk (`#disputes-tab`)
* Review contested consignments (e.g., Order `GEM-ORD-2026-8804`: 75-inch Interactive Touch Panel).
* Analyze side-by-side claims: Consignee unpacked scratch claim vs. Vendor factory seal verification.
* Settle disputes as the Nodal Officer via **"Approve Return (Refund Buyer)"** or **"Reject Return (Uphold Seller)"**.

### 3. 🔄 Three-Source Ledger Reconciliation Matrix (`#reconciliation-tab`)
* Displays cross-ledger states between Seller Portals, Payment Gateways, and Treasury logs.
* Distinguishes between normal settlement delay (**WAITING**) and prolonged latency (**STUCK - Auto-Escalated**).

### 4. 🔬 15 Seeded Stress Edge Cases (`#anomalies-tab`)
* Interactive verification deck detailing all 15 planted exceptions (ghost couriers, tampered barcode checksums, voucher expirations, and heavy-returner friction tiers).

### 5. 📜 Cryptographic Audit Ledger (`#audit-tab`)
* Transparent transaction log recording timestamp, actor, state transition, and SHA-256 cryptographic digest for complete legal auditability.

---

## 🛠️ Technical Architecture & Stack

* **Frontend:** Single Page Application (SPA) adhering to National Government Design Standards (Deep Navy `#0B2545`, Ashoka Gold `#C88A1E`, National Tricolor accents, system-native typography for zero layout shifts). Deployed on **Vercel Edge Network**.
* **Backend:** Lightweight, asynchronous Python REST API providing state reconciliation, idempotency verification, and multi-instrument waterfall allocation. Deployed on **Render**.
* **Resilience Layer:** Integrated browser state cache ensures full UI interactivity even under unstable network conditions during live demonstrations.

---

## 🧪 Evaluation & Test Harness

Run the verification harness locally to validate all 15 planted edge cases:

```bash
# Navigate to the project root
cd gem_pratyarpan

# Execute the test suite
python verification_harness.py

EXPECTED OUTPUT:
================================================================
 GeM Pratyarpan - IMPACTX 2026 Test Harness
================================================================
Total Seeded Anomalies Verified: 15
[TEST PASS] ANOM-01: Duplicate Refund Idempotency Retry
[TEST PASS] ANOM-02: Three-Way Status Disagreement
[TEST PASS] ANOM-03: Courier Ghost Delivery / Premises Closed Dispute
[TEST PASS] ANOM-04: Visual Inspection Scratch Dispute
[TEST PASS] ANOM-05: Expired Subsidy Voucher Reversal
[TEST PASS] ANOM-06: Partial Return Bundled Tier Reallocation
[TEST PASS] ANOM-07: Legitimate Heavy Returner False Positive
[TEST PASS] ANOM-08: Gateway Timeout During Ledger Release
[TEST PASS] ANOM-09: Multi-Split Rounding Discrepancy
[TEST PASS] ANOM-10: Tampered Tracking Consignment Code
[TEST PASS] ANOM-11: Weight Discrepancy Handover
[TEST PASS] ANOM-12: Dormant / Closed Treasury Account
[TEST PASS] ANOM-13: Mid-Transit Revocation by Buyer
[TEST PASS] ANOM-14: Statutory SLA Breach by Inspector
[TEST PASS] ANOM-15: Concurrent Admin Override vs System Auto-Reconcile
----------------------------------------------------------------
Pass Rate: 15/15 Passed (100% Reliability)
Idempotency Guard: Verified
Append-Only Audit Hash: Verified
================================================================









