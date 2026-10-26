#!/usr/bin/env python3
"""
Generate Evidence Index (PDF and Markdown) for The Hungry Helm Phase 2
Mapping all genuine Jira screenshots (7) and full application screenshots (13)
Student: Prikshit Sharma | Enrollment: S24CSEU1823 | Course: CSET455
Faculty: Rashmi Rani | Bennett University
"""

import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.pdfgen import canvas

TEAL = colors.HexColor("#1a5f5a")
DEEP_SLATE = colors.HexColor("#264653")
GOLD = colors.HexColor("#b8860b")
DARK_CHARCOAL = colors.HexColor("#172b4d")
MUTED_GREY = colors.HexColor("#5e6c84")
BG_LIGHT = colors.HexColor("#f4f5f7")
BORDER_LIGHT = colors.HexColor("#dfe1e6")
WHITE = colors.HexColor("#ffffff")

md_content = """# The Hungry Helm — Phase 2 Evidence Index & Screenshot Mapping
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
"""

with open("docs/phase2/evidence/evidence_index.md", "w") as f:
    f.write(md_content)

# Now build PDF
class IndexNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_header_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(MUTED_GREY)
        self.setStrokeColor(BORDER_LIGHT)
        self.setLineWidth(0.6)
        self.line(46, 42, 8.5 * inch - 46, 42)
        self.drawString(46, 30, "The Hungry Helm (THH) • Phase 2 Evidence Index • Student: Prikshit Sharma (S24CSEU1823)")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 46, 30, page_str)
        self.restoreState()

pdf_filename = "Hungry_Helm_Evidence_Index.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter, leftMargin=46, rightMargin=46, topMargin=46, bottomMargin=46)
styles = getSampleStyleSheet()

title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=TEAL, spaceAfter=2)
sub_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=GOLD, spaceAfter=5)
h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=9.5, leading=12, textColor=DEEP_SLATE, spaceBefore=6, spaceAfter=3, keepWithNext=True)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=7.2, leading=9.5, textColor=DARK_CHARCOAL, spaceAfter=3)
th_style = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.0, leading=8.5, textColor=WHITE)
td_style = ParagraphStyle('TD', parent=styles['Normal'], fontName='Helvetica', fontSize=6.5, leading=8.0, textColor=DARK_CHARCOAL)
td_bold = ParagraphStyle('TDBold', parent=td_style, fontName='Helvetica-Bold')

elements = []
elements.append(Paragraph("THE HUNGRY HELM — PHASE 2 EVIDENCE INDEX (JIRA & RUNNING APP)", title_style))
elements.append(Paragraph("<b>CSET455 Agile Software Development • Faculty: Rashmi Rani • Student: Prikshit Sharma (S24CSEU1823) • Batch 46</b>", sub_style))
elements.append(Paragraph("<b>Live Jira Site:</b> https://prikshittt777.atlassian.net (Key: THH, Board ID: 167) | <b>App:</b> http://localhost:3000<br/>"
                          "This document provides a comprehensive mapping of all genuine screenshots (7 Jira Desktop captures + 13 Live Application views) to the report figures.", body_style))
elements.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=5))

elements.append(Paragraph("1. Primary Jira Desktop Screenshots (7 High-DPI Retina Captures)", h2_style))
t1_head = [Paragraph("File Name", th_style), Paragraph("Jira View", th_style), Paragraph("Content Verified", th_style), Paragraph("Report Figure", th_style)]
t1_rows = [
    [Paragraph("jira_timeline.png", td_bold), Paragraph("Jira Timeline", td_style), Paragraph("Sprints 1 to 4 bars across Oct, Nov & Dec; 7 Epics (THH-1 to THH-8)", td_style), Paragraph("Figure 1", td_bold)],
    [Paragraph("jira_epic_list.png", td_bold), Paragraph("Jira List View", td_style), Paragraph("7 Epics with keys, assignees (Prikshit Sharma), priorities & status", td_style), Paragraph("Figure 2", td_bold)],
    [Paragraph("jira_backlog_sprints_1_2.png", td_bold), Paragraph("Jira Backlog", td_style), Paragraph("THH Sprint 1 — Foundation (12–26 Oct, 4 items) & Sprint 2 (26 Oct–8 Nov, 4 items)", td_style), Paragraph("Figure 3", td_bold)],
    [Paragraph("jira_backlog_sprints_3_4.png", td_bold), Paragraph("Jira Backlog", td_style), Paragraph("THH Sprint 3 — KDS (9–22 Nov, 3 items) & Sprint 4 (23 Nov–6 Dec, 3 items)", td_style), Paragraph("Figure 6", td_bold)],
    [Paragraph("jira_backlog_remaining_thh2.png", td_bold), Paragraph("Jira Backlog", td_style), Paragraph("Remaining unallocated backlog item THH-2 Multi-Outlet Seed & Data Model (3 SP)", td_style), Paragraph("Figure 8", td_bold)],
    [Paragraph("jira_summary_dashboard.png", td_bold), Paragraph("Jira Summary", td_style), Paragraph("22 Total work items: 2 Done, 1 In Progress, 19 To Do", td_style), Paragraph("Figure 10 & 27", td_bold)],
    [Paragraph("jira_reports.png", td_bold), Paragraph("Jira Reports", td_style), Paragraph("Work items by status, issue types, assignee distribution & cycle-time metrics", td_style), Paragraph("Figure 11 & 33", td_bold)]
]
t1 = Table([t1_head] + t1_rows, colWidths=[1.7 * inch, 1.2 * inch, 3.4 * inch, 0.9 * inch])
t1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TEAL),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 1.8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8),
]))
elements.append(t1)
elements.append(Spacer(1, 4))

elements.append(PageBreak())

elements.append(Paragraph("2. Live Application Implementation Screenshots (13 High-Resolution Retina Captures)", h2_style))
t2_head = [Paragraph("File Name", th_style), Paragraph("Application Screen", th_style), Paragraph("Technical Capability Demonstrated", th_style), Paragraph("Report Figure", th_style)]
t2_rows = [
    [Paragraph("01_student_login_screen.png", td_bold), Paragraph("Student Login Gateway", td_style), Paragraph("Restricts login to @bennett.edu.in accounts, prefilled credentials, JWT signing", td_style), Paragraph("Figure 4 & App-1", td_bold)],
    [Paragraph("02_staff_login_tab.png", td_bold), Paragraph("Staff Login Gateway", td_style), Paragraph("Multi-tenant stall authority authentication with outlet dropdown & secure PIN", td_style), Paragraph("Figure App-2", td_bold)],
    [Paragraph("03_nautical_campus_chart.png", td_bold), Paragraph("Nautical Food Chart", td_style), Paragraph("5 campus food stalls with live queue badges, wait estimates, and status pills", td_style), Paragraph("Figure 5a & App-3", td_bold)],
    [Paragraph("04_port_details_drawer.png", td_bold), Paragraph("Slide-out Port Drawer", td_style), Paragraph("Real-time drawer showing stall hours, rating, cuisine, and quick-order list", td_style), Paragraph("Figure App-4", td_bold)],
    [Paragraph("05_outlet_menu_browsing.png", td_bold), Paragraph("Categorized Menu", td_style), Paragraph("Category navigation (Mains, Rice, Drinks), veg/non-veg tags, and descriptions", td_style), Paragraph("Figure 5b & App-5", td_bold)],
    [Paragraph("06_cart_with_items.png", td_bold), Paragraph("Persistent Cart", td_style), Paragraph("Interactive cart panel displaying items, quantity buttons (+/-), and total (₹490)", td_style), Paragraph("Figure App-6", td_bold)],
    [Paragraph("07_order_confirmation_dialog.png", td_bold), Paragraph("Confirmation Modal", td_style), Paragraph("Modal confirming order breakdown, instructions, and token reservation", td_style), Paragraph("Figure App-7", td_bold)],
    [Paragraph("08_voyage_log_my_orders.png", td_bold), Paragraph("Student Voyage Log", td_style), Paragraph("Live tracking showing token #IK-104, 4-stage state machine (Preparing in Galley)", td_style), Paragraph("Figure 7b & App-8", td_bold)],
    [Paragraph("09_staff_kds_board.png", td_bold), Paragraph("Staff Kitchen KDS", td_style), Paragraph("Live kitchen terminal with Incoming, Preparing, and Ready columns & timers", td_style), Paragraph("Figure 7a & App-9", td_bold)],
    [Paragraph("10_staff_menu_manifest_editor.png", td_bold), Paragraph("Menu Manifest Editor", td_style), Paragraph("Stall management allowing staff to toggle stock availability and add dishes", td_style), Paragraph("Figure App-10", td_bold)],
    [Paragraph("11_staff_analytics_revenue.png", td_bold), Paragraph("Staff Daily Analytics", td_style), Paragraph("KPI dashboard: Revenue (₹8,240), Orders (47), 14m Avg Wait, Top Dishes, Peak Hours", td_style), Paragraph("Figure 9 & App-11", td_bold)],
    [Paragraph("12_gateway_role_selection.png", td_bold), Paragraph("Role Selection Portal", td_style), Paragraph("Role routing portal routing visitors between Student Helm and Staff Port Authority", td_style), Paragraph("Figure App-12", td_bold)],
    [Paragraph("13_darkmode_prototype.png", td_bold), Paragraph("Dark Mode Prototype", td_style), Paragraph("Night theme architectural prototype for evening and late-night campus dining", td_style), Paragraph("Figure App-13", td_bold)]
]
t2 = Table([t2_head] + t2_rows, colWidths=[1.8 * inch, 1.4 * inch, 3.1 * inch, 0.9 * inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TEAL),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 1.5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
]))
elements.append(t2)
elements.append(Spacer(1, 4))

elements.append(Paragraph("3. Technical Verification & Integrity Summary", h2_style))
elements.append(Paragraph(
    "• <b>Snapshot Consistency:</b> The report reflects the exact snapshot state shown in the Desktop screenshots: 22 total items, 2 completed, 1 in progress, 19 to do.<br/>"
    "• <b>Sprint Timeline Integrity:</b> Sprints are documented with genuine scheduled dates: Sprint 1 (12–26 Oct), Sprint 2 (26 Oct–8 Nov), Sprint 3 (9–22 Nov), Sprint 4 (23 Nov–6 Dec).<br/>"
    "• <b>Verified Codebase Facts:</b> Multi-outlet seed data verified in <code>backend/config/seed.js</code>; in-memory fallback verified in <code>backend/server.js</code>; Bennett email login verified in <code>backend/controllers/authController.js</code>; server-side price calculation verified in <code>backend/controllers/orderController.js</code>; port 5001 migration verified to prevent AirPlay port conflicts.",
    body_style
))

doc.build(elements, canvasmaker=IndexNumberedCanvas)

# Mirror PDF to Desktop and Downloads
shutil.copyfile(pdf_filename, f"/Users/prikshit/Desktop/{pdf_filename}")
shutil.copyfile(pdf_filename, f"/Users/prikshit/Downloads/{pdf_filename}")
print("Successfully generated updated Hungry_Helm_Evidence_Index.pdf and evidence_index.md, mirrored to Desktop and Downloads.")
