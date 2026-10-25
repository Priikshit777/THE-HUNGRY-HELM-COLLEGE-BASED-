# The Hungry Helm — Phase 2 Evidence Index & Screenshot Mapping
**Course:** CSET455 Agile Software Development  
**Student:** Prikshit Sharma (S24CSEU1823) | Batch 46  
**Faculty Evaluator:** Rashmi Rani  
**Jira Site:** https://prikshittt777.atlassian.net | Project: The Hungry Helm (`THH`) | Board ID: `167`

---

## 1. Primary Jira Desktop Screenshots

| File Name | Jira View | Content Verified | Report Figure | Template Section |
| :--- | :--- | :--- | :--- | :--- |
| `jira_timeline.png` | **Jira Timeline** | Sprints 1 to 4 bars across Oct, Nov & Dec; 7 Epics (`THH-1` to `THH-8`) | Figure 1 | Section 1.2 (Epics / Roadmap) |
| `jira_epic_list.png` | **Jira List View** | 7 Epics with keys, assignees (Prikshit Sharma), priorities & status | Figure 2 | Section 2 (Product Backlog) |
| `jira_backlog_sprints_1_2.png` | **Jira Backlog** | `THH Sprint 1 — Foundation` (12–26 Oct, 4 items) & `THH Sprint 2 — Ordering` (26 Oct–8 Nov, 4 items) | Figure 3 | Section 3.1 & 3.2 (Sprint Backlog) |
| `jira_backlog_sprints_3_4.png` | **Jira Backlog** | `THH Sprint 3 — KDS & Status` (9–22 Nov, 3 items) & `THH Sprint 4 — Hardening` (23 Nov–6 Dec, 3 items) | Figure 5 | Section 3.3 & 3.4 (Sprint Backlog) |
| `jira_backlog_remaining_thh2.png` | **Jira Backlog** | Remaining unallocated item `THH-2 Multi-Outlet Seed & Campus Data Model` (3 SP) | Figure 7 | Section 3.4 (Backlog Pool) |
| `jira_summary_dashboard.png` | **Jira Summary** | 22 Total work items: **2 Done, 1 In Progress, 19 To Do** | Figure 8 & 27 | Section 4.6 (Dashboard) & Section 5 |
| `jira_reports.png` | **Jira Reports** | Work items by status, issue types, assignee distribution & cycle time | Figure 9 & 33 | Section 4.2, 4.3 & Section 5 |

---

## 2. Running Application Deliverable Screenshots

| File Name | Application View | Port & Endpoint | Demonstrated Capability | Report Figure |
| :--- | :--- | :--- | :--- | :--- |
| `deliverable_s1_foodchart.png` | Campus Food Chart | `http://localhost:3000` | 5 campus stalls (Kathis, Chai Garam, Southern Stories, Burgrill, Nescafe) with live wait time badges | Figure 4 |
| `deliverable_s3_kds.png` | Kitchen Display System | `http://localhost:3000/kds.html` | Staff terminal advancing meal tokens through 4-stage FIFO order state machine | Figure 6 |

---

## 3. Technical Verification & Integrity Summary

1. **Snapshot Consistency:** The report reflects the exact snapshot state shown in the Desktop screenshots: 22 total items, 2 completed, 1 in progress, 19 to do.
2. **Sprint Timeline Integrity:** Sprints are documented with genuine scheduled dates: Sprint 1 (12–26 Oct), Sprint 2 (26 Oct–8 Nov), Sprint 3 (9–22 Nov), Sprint 4 (23 Nov–6 Dec).
3. **Verified Codebase Facts:** 
   - Multi-outlet seed data verified in `backend/config/seed.js` and `backend/server.js`.
   - In-memory database fallback verified in `backend/server.js`.
   - Bennett email authentication restriction verified in `backend/controllers/authController.js`.
   - Server-side price calculation verified in `backend/controllers/orderController.js`.
