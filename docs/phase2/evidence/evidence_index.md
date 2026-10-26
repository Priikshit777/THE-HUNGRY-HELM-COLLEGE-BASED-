# The Hungry Helm — Phase 2 Evidence Index & Screenshot Mapping
**Course:** CSET455 Agile Software Development  
**Student:** Prikshit Sharma (S24CSEU1823) | Batch 46  
**Faculty Evaluator:** Rashmi Rani  
**Jira Site:** https://prikshittt777.atlassian.net | Project: The Hungry Helm (`THH`) | Board ID: `167`
**Application Ports:** Frontend at `http://localhost:3000` | Backend API at `http://localhost:5001` (In-Memory MongoDB Fallback)

---

## 1. Primary Jira Desktop Screenshots (7 High-DPI Retina Captures)

| File Name | Jira View | Content Verified | Report Figure | Template Section |
| :--- | :--- | :--- | :--- | :--- |
| `jira_timeline.png` | **Jira Timeline** | Sprints 1 to 4 bars across Oct, Nov & Dec; 7 Epics (`THH-1` to `THH-8`) | Figure 1 | Section 1.2 (Epics / Roadmap) |
| `jira_epic_list.png` | **Jira List View** | 7 Epics with keys, assignees (Prikshit Sharma), priorities & status | Figure 2 | Section 2 (Product Backlog) |
| `jira_backlog_sprints_1_2.png` | **Jira Backlog** | `THH Sprint 1 — Foundation` (12–26 Oct, 4 items) & `THH Sprint 2 — Ordering` (26 Oct–8 Nov, 4 items) | Figure 3 | Section 3.1 & 3.2 (Sprint Backlog) |
| `jira_backlog_sprints_3_4.png` | **Jira Backlog** | `THH Sprint 3 — KDS & Status` (9–22 Nov, 3 items) & `THH Sprint 4 — Hardening` (23 Nov–6 Dec, 3 items) | Figure 6 | Section 3.3 & 3.4 (Sprint Backlog) |
| `jira_backlog_remaining_thh2.png` | **Jira Backlog** | Remaining unallocated item `THH-2 Multi-Outlet Seed & Campus Data Model` (3 SP) | Figure 8 | Section 3.4 (Backlog Pool) |
| `jira_summary_dashboard.png` | **Jira Summary** | 22 Total work items: **2 Done, 1 In Progress, 19 To Do** | Figure 10 & 27 | Section 4.6 (Dashboard) & Section 5 |
| `jira_reports.png` | **Jira Reports** | Work items by status, issue types, assignee distribution & cycle time | Figure 11 & 33 | Section 4.2, 4.3 & Section 5 |

---

## 2. Live Application Implementation Screenshots (13 High-DPI Captures)

| File Name | Application Screen | Endpoint / Context | Technical Capability Demonstrated | Figure in Report |
| :--- | :--- | :--- | :--- | :--- |
| `01_student_login_screen.png` | Student Login Gateway | `http://localhost:3000/index.html` | Restricts login to `@bennett.edu.in` accounts, prefilled demo credentials, JWT signing | Figure 4 & App-1 |
| `02_staff_login_tab.png` | Staff Login Gateway | `http://localhost:3000/index.html` | Multi-tenant stall authority authentication with outlet dropdown & secure PIN | Figure App-2 |
| `03_nautical_campus_chart.png` | Nautical Food Chart | `http://localhost:3000/index.html` | 5 campus food stalls (Infinity Kitchens, House of Chow, Hotspot, Snapeats, Southern Stories) with wait badges | Figure 5a & App-3 |
| `04_port_details_drawer.png` | Slide-out Port Drawer | `http://localhost:3000/index.html` | Real-time drawer displaying outlet operating hours, rating, cuisine, and quick-order list | Figure App-4 |
| `05_outlet_menu_browsing.png` | Categorized Outlet Menu | `http://localhost:3000/index.html` | Full menu with category navigation (Mains, Rice, Drinks), veg/non-veg tags, and descriptions | Figure 5b & App-5 |
| `06_cart_with_items.png` | Persistent Shopping Cart | `http://localhost:3000/index.html` | Interactive cart panel displaying items, quantity buttons (+/-), and live total calculation (₹490) | Figure App-6 |
| `07_order_confirmation_dialog.png` | Order Confirmation Modal | `http://localhost:3000/index.html` | Checkout modal confirming order breakdown, delivery/pickup instructions, and token reservation | Figure App-7 |
| `08_voyage_log_my_orders.png` | Student Voyage Log | `http://localhost:3000/index.html` | Live tracking showing token `#IK-104`, 4-stage state machine (Preparing in Galley), and past receipts | Figure 7b & App-8 |
| `09_staff_kds_board.png` | Staff Kitchen Display (KDS) | `http://localhost:3000/index.html` | Live kitchen terminal with Incoming, Preparing, and Ready columns with timer and handover triggers | Figure 7a & App-9 |
| `10_staff_menu_manifest_editor.png` | Staff Menu Manifest Editor | `http://localhost:3000/index.html` | Direct stall management allowing staff to toggle stock availability and add new menu items | Figure App-10 |
| `11_staff_analytics_revenue.png` | Staff Daily Analytics | `http://localhost:3000/index.html` | KPI dashboard: Revenue (₹8,240), Orders (47), 14m Avg Wait, Top Dishes ranking, Peak Hours chart | Figure 9 & App-11 |
| `12_gateway_role_selection.png` | Dual-Role Selection Portal | `http://localhost:3000/gateway.html` | Role routing portal allowing campus visitors to choose between Student Helm and Staff Port Authority | Figure App-12 |
| `13_darkmode_prototype.png` | Dark Mode Theme Prototype | `http://localhost:3000/archive_prototype_darkmode/index.html` | Night theme architectural prototype for evening and late-night campus dining | Figure App-13 |

---

## 3. Technical Verification & Integrity Summary

1. **Snapshot Consistency:** The report reflects the exact snapshot state shown in the Desktop screenshots: 22 total items, 2 completed, 1 in progress, 19 to do.
2. **Sprint Timeline Integrity:** Sprints are documented with genuine scheduled dates: Sprint 1 (12–26 Oct), Sprint 2 (26 Oct–8 Nov), Sprint 3 (9–22 Nov), Sprint 4 (23 Nov–6 Dec).
3. **Verified Codebase Facts:** 
   - Multi-outlet seed data verified in `backend/config/seed.js` and `backend/server.js`.
   - In-memory database fallback (`mongodb-memory-server`) verified in `backend/server.js`.
   - Bennett email authentication restriction verified in `backend/controllers/authController.js`.
   - Server-side price calculation verified in `backend/controllers/orderController.js`.
   - Port 5001 migration permanently verified to eliminate macOS AirPlay Receiver port 5000 collisions.
