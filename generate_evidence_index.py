#!/usr/bin/env python3
"""
Generate Hungry_Helm_Evidence_Index.pdf
Maps every Jira evidence artifact to its CSET455 Lab, Report Section, and verified Live Jira object.
"""

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
SUCCESS_GREEN = colors.HexColor("#006644")
WHITE = colors.HexColor("#ffffff")

def build_index():
    pdf_filename = "Hungry_Helm_Evidence_Index.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54, rightMargin=54,
        topMargin=54, bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=TEAL,
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=GOLD,
        spaceAfter=10
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=DARK_CHARCOAL
    )
    
    th_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=WHITE
    )
    
    tc_style = ParagraphStyle(
        'TC',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10,
        textColor=DARK_CHARCOAL
    )
    
    elements = []
    
    elements.append(Paragraph("THE HUNGRY HELM — JIRA EVIDENCE ARTIFACT INDEX", title_style))
    elements.append(Paragraph("<b>CSET455 Agile Software Development | Phase 2 Evaluation | Student: Prikshit Sharma (S24CSEU1823)</b>", subtitle_style))
    elements.append(Paragraph(
        "<b>Live Jira Workspace:</b> <font color='#0052cc'><u>https://prikshittt777.atlassian.net</u></font>  •  <b>Project:</b> The Hungry Helm (Key: <b>THH</b>, ID: <b>10166</b>)  •  <b>Board ID:</b> <b>167</b><br/>"
        "This document indexes the genuine Jira implementation artifacts captured from the live Jira Cloud workspace, mapping each screenshot directly to its corresponding syllabus lab, report figure, and verified platform entity.",
        body_style
    ))
    elements.append(Spacer(1, 10))
    
    index_data = [
        [Paragraph("Artifact Filename", th_style), Paragraph("Lab Mapping", th_style), Paragraph("Report Figure & Section", th_style), Paragraph("Live Jira Object & Verification Details", th_style)],
        [
            Paragraph("<b>01_jira_product_backlog_epics.png</b>", tc_style),
            Paragraph("<b>Lab 1 & Lab 2</b><br/>Tool Setup & Requirements", tc_style),
            Paragraph("<b>Figure 1</b><br/>Section 2: Backlog & INVEST", tc_style),
            Paragraph("Live Project <b>THH</b> (10166): 6 Epics (<code>THH-3</code> to <code>THH-8</code>), 14 User Stories (<code>THH-9</code> to <code>THH-22</code>), Fibonacci story point sizing, priority ranking, and epic color associations.", tc_style)
        ],
        [
            Paragraph("<b>02_jira_sprint_planning_4_sprints.png</b>", tc_style),
            Paragraph("<b>Lab 3 & Lab 6</b><br/>Sizing & Velocity Planning", tc_style),
            Paragraph("<b>Figure 2</b><br/>Section 4: Four Sprints", tc_style),
            Paragraph("Board <b>167</b> Backlog: 4 structured 2-week Sprints (Sprint 140: 18 pts active; Sprint 141: 18 pts; Sprint 142: 18 pts; Sprint 143: 13 pts hardening). Each sprint contains verified Sprint Goals.", tc_style)
        ],
        [
            Paragraph("<b>03_jira_active_scrum_board.png</b>", tc_style),
            Paragraph("<b>Lab 4</b><br/>Scrum Board & Flow", tc_style),
            Paragraph("<b>Figure 3</b><br/>Section 5: Scrum Board", tc_style),
            Paragraph("Board <b>167</b> Active Sprint: <code>THH Sprint 1 - Foundation</code> (ID: 140). Verified real card distribution: <code>THH-9</code> (Done), <code>THH-10</code> (Done), <code>THH-11</code> (In Progress), <code>THH-12</code> (To Do).", tc_style)
        ],
        [
            Paragraph("<b>04_jira_issue_detail_acceptance_criteria.png</b>", tc_style),
            Paragraph("<b>Lab 2 & Lab 6</b><br/>Story Engineering & DoD", tc_style),
            Paragraph("<b>Figure 4</b><br/>Section 7: Story Detail & DoD", tc_style),
            Paragraph("Issue <code>THH-16</code> Detail view: Cryptographically Verified Server-Side Checkout. Shows BDD Given/When/Then acceptance criteria, 5.0 Story Points, Epic link <code>THH-6</code>, and 6-point Definition of Done audit.", tc_style)
        ],
        [
            Paragraph("<b>05_jira_custom_workflow_rules.png</b>", tc_style),
            Paragraph("<b>Lab 5 & Lab 7</b><br/>Custom Workflow & Rules", tc_style),
            Paragraph("<b>Figure 5</b><br/>Section 6: Workflow Governance", tc_style),
            Paragraph("Workflow <code>THH_Software_Scrum_Workflow</code>: Configured with 5 statuses (Backlog, To Do, In Progress, In Review/QA, Done), project role conditions, Fix Version validators, and QA defect rejection loops.", tc_style)
        ],
        [
            Paragraph("<b>06_jira_custom_dashboard_gadgets.png</b>", tc_style),
            Paragraph("<b>Lab 8</b><br/>Agile Reporting Dashboard", tc_style),
            Paragraph("<b>Figure 6</b><br/>Section 8: Agile Dashboard", tc_style),
            Paragraph("Dashboard <b>10001</b> (The Hungry Helm - Agile Delivery Dashboard): 4 active gadgets (Sprint Burndown 10004, Created vs. Resolved 10005, Two-Dimensional Filter Stats 10006, Sprint Health 10007).", tc_style)
        ],
        [
            Paragraph("<b>07_jira_burndown_and_velocity_reports.png</b>", tc_style),
            Paragraph("<b>Lab 6 & Lab 8</b><br/>Burndown & Velocity", tc_style),
            Paragraph("<b>Figure 7</b><br/>Section 6: Release Metrics", tc_style),
            Paragraph("Board <b>167</b> Reports: Sprint 1 Burndown showing 8 pts completed vs 10 pts in flight; 4-Sprint velocity commitment tracking respecting 20 pt team capacity and 7 pt Hardening reserve.", tc_style)
        ]
    ]
    
    table = Table(index_data, colWidths=[130, 85, 95, 194])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), TEAL),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1, BORDER_LIGHT),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, BG_LIGHT]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 14))
    
    # Summary of live URLs
    elements.append(Paragraph("<b>Direct Live URLs for Tomorrow's Evaluation:</b>", ParagraphStyle('H2', parent=body_style, fontName='Helvetica-Bold', fontSize=9, textColor=DEEP_SLATE)))
    urls = [
        "• <b>Backlog URL:</b> https://prikshittt777.atlassian.net/jira/software/c/projects/THH/boards/167/backlog",
        "• <b>Active Scrum Board URL:</b> https://prikshittt777.atlassian.net/jira/software/c/projects/THH/boards/167",
        "• <b>Dashboard URL:</b> https://prikshittt777.atlassian.net/jira/dashboards/10001",
        "• <b>Project Settings URL:</b> https://prikshittt777.atlassian.net/jira/software/c/projects/THH/settings/details"
    ]
    for u in urls:
        elements.append(Paragraph(u, body_style))
        
    doc.build(elements)
    print("Successfully built Hungry_Helm_Evidence_Index.pdf")

if __name__ == "__main__":
    build_index()
