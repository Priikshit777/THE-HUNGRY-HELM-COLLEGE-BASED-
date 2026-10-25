#!/usr/bin/env python3
"""
Generate Evidence Index (PDF and Markdown) for The Hungry Helm Phase 2
Mapping all genuine screenshots found on Desktop to report figures and requirements.
Student: Prikshit Sharma | Enrollment: S24CSEU1823 | Course: CSET455
Faculty: Rashmi Rani | Bennett University
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
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

doc = SimpleDocTemplate("Hungry_Helm_Evidence_Index.pdf", pagesize=letter, leftMargin=46, rightMargin=46, topMargin=46, bottomMargin=46)
styles = getSampleStyleSheet()

title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=TEAL, spaceAfter=2)
sub_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=GOLD, spaceAfter=6)
h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=DEEP_SLATE, spaceBefore=8, spaceAfter=4, keepWithNext=True)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=10, textColor=DARK_CHARCOAL, spaceAfter=4)
th_style = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.2, leading=9, textColor=WHITE)
td_style = ParagraphStyle('TD', parent=styles['Normal'], fontName='Helvetica', fontSize=6.8, leading=8.5, textColor=DARK_CHARCOAL)
td_bold = ParagraphStyle('TDBold', parent=td_style, fontName='Helvetica-Bold')

elements = []
elements.append(Paragraph("THE HUNGRY HELM — PHASE 2 EVIDENCE INDEX", title_style))
elements.append(Paragraph("<b>CSET455 Agile Software Development • Faculty: Rashmi Rani • Student: Prikshit Sharma (S24CSEU1823)</b>", sub_style))
elements.append(Paragraph("<b>Live Jira Site:</b> https://prikshittt777.atlassian.net (Key: THH, Board ID: 167, Dashboard ID: 10001)<br/>"
                          "This document maps all genuine screenshots found on the MacBook Air Desktop to the Phase 2 Evaluation Report figures and syllabus requirements.", body_style))
elements.append(HRFlowable(width="100%", thickness=1, color=TEAL, spaceAfter=6))

elements.append(Paragraph("1. Primary Jira Desktop Screenshots (High-DPI Retina Captures)", h2_style))
t1_head = [Paragraph("File Name", th_style), Paragraph("Jira View", th_style), Paragraph("Content Verified", th_style), Paragraph("Report Figure", th_style)]
t1_rows = [
    [Paragraph("jira_timeline.png", td_bold), Paragraph("Jira Timeline", td_style), Paragraph("Sprints 1 to 4 bars across Oct, Nov & Dec; 7 Epics (THH-1 to THH-8)", td_style), Paragraph("Figure 1", td_bold)],
    [Paragraph("jira_epic_list.png", td_bold), Paragraph("Jira List View", td_style), Paragraph("7 Epics with keys, assignees (Prikshit Sharma), priorities & status", td_style), Paragraph("Figure 2", td_bold)],
    [Paragraph("jira_backlog_sprints_1_2.png", td_bold), Paragraph("Jira Backlog", td_style), Paragraph("THH Sprint 1 — Foundation (12–26 Oct, 4 items) & Sprint 2 (26 Oct–8 Nov, 4 items)", td_style), Paragraph("Figure 3", td_bold)],
    [Paragraph("jira_backlog_sprints_3_4.png", td_bold), Paragraph("Jira Backlog", td_style), Paragraph("THH Sprint 3 — KDS (9–22 Nov, 3 items) & Sprint 4 (23 Nov–6 Dec, 3 items)", td_style), Paragraph("Figure 5", td_bold)],
    [Paragraph("jira_backlog_remaining_thh2.png", td_bold), Paragraph("Jira Backlog", td_style), Paragraph("Remaining unallocated backlog item THH-2 Multi-Outlet Seed & Data Model (3 SP)", td_style), Paragraph("Figure 7", td_bold)],
    [Paragraph("jira_summary_dashboard.png", td_bold), Paragraph("Jira Summary", td_style), Paragraph("22 Total work items: 2 Done, 1 In Progress, 19 To Do", td_style), Paragraph("Figure 8 & 27", td_bold)],
    [Paragraph("jira_reports.png", td_bold), Paragraph("Jira Reports", td_style), Paragraph("Work items by status, issue types, assignee distribution & cycle-time metrics", td_style), Paragraph("Figure 9 & 33", td_bold)]
]
t1 = Table([t1_head] + t1_rows, colWidths=[1.7 * inch, 1.2 * inch, 3.4 * inch, 0.9 * inch])
t1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TEAL),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
]))
elements.append(t1)
elements.append(Spacer(1, 6))

elements.append(Paragraph("2. Running Application Deliverable Screenshots", h2_style))
t2_head = [Paragraph("File Name", th_style), Paragraph("Endpoint", th_style), Paragraph("Demonstrated Capability", th_style), Paragraph("Report Figure", th_style)]
t2_rows = [
    [Paragraph("deliverable_s1_foodchart.png", td_bold), Paragraph("http://localhost:3000", td_style), Paragraph("5 campus stalls (Kathis, Chai Garam, Southern Stories, Burgrill, Nescafe) with live badges", td_style), Paragraph("Figure 4", td_bold)],
    [Paragraph("deliverable_s3_kds.png", td_bold), Paragraph("http://localhost:3000/kds.html", td_style), Paragraph("Staff terminal advancing meal tokens through 4-stage FIFO order state machine", td_style), Paragraph("Figure 6", td_bold)]
]
t2 = Table([t2_head] + t2_rows, colWidths=[1.8 * inch, 1.4 * inch, 3.1 * inch, 0.9 * inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), TEAL),
    ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 2),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
]))
elements.append(t2)
elements.append(Spacer(1, 6))

elements.append(Paragraph("3. Technical Verification & Integrity Summary", h2_style))
elements.append(Paragraph(
    "• <b>Snapshot Consistency:</b> The report reflects the exact snapshot state shown in the Desktop screenshots: 22 total items, 2 completed, 1 in progress, 19 to do.<br/>"
    "• <b>Sprint Timeline Integrity:</b> Sprints are documented with genuine scheduled dates: Sprint 1 (12–26 Oct), Sprint 2 (26 Oct–8 Nov), Sprint 3 (9–22 Nov), Sprint 4 (23 Nov–6 Dec).<br/>"
    "• <b>Verified Codebase Facts:</b> Multi-outlet seed data verified in <code>backend/config/seed.js</code>; in-memory fallback verified in <code>backend/server.js</code>; Bennett email login verified in <code>backend/controllers/authController.js</code>; server-side price calculation verified in <code>backend/controllers/orderController.js</code>.",
    body_style
))

doc.build(elements, canvasmaker=IndexNumberedCanvas)
print("Successfully generated updated Hungry_Helm_Evidence_Index.pdf and evidence_index.md")

