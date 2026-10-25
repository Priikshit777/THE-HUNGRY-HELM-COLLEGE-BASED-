#!/usr/bin/env python3
"""
Generate Viva Defense Preparation Guide PDF for The Hungry Helm
Student: Prikshit Sharma | Enrollment: S24CSEU1823 | Course: CSET455
Faculty: Rashmi Rani | Bennett University
"""

import sys
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

class VivaNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(VivaNumberedCanvas, self).__init__(*args, **kwargs)
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
        
        if self._pageNumber > 1:
            self.drawString(54, 11 * inch - 36, "THE HUNGRY HELM — VIVA VOCE DEFENSE & DEMONSTRATION GUIDE")
            self.drawRightString(8.5 * inch - 54, 11 * inch - 36, "CSET455 PHASE 2")
            self.setStrokeColor(BORDER_LIGHT)
            self.setLineWidth(0.6)
            self.line(54, 11 * inch - 42, 8.5 * inch - 54, 11 * inch - 42)
            
        self.setStrokeColor(BORDER_LIGHT)
        self.setLineWidth(0.6)
        self.line(54, 46, 8.5 * inch - 54, 46)
        self.drawString(54, 34, "Student: Prikshit Sharma (S24CSEU1823)  •  Project: The Hungry Helm (THH | Board 167)")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 54, 34, page_str)
        self.restoreState()

def build_viva_guide():
    pdf_filename = "Prikshit_Sharma_HungryHelm_Viva_Guide.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54, rightMargin=54,
        topMargin=54, bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=TEAL, spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=14,
        textColor=GOLD, spaceAfter=10
    )
    h1_style = ParagraphStyle(
        'SectionH1', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=11.5, leading=15.5,
        textColor=TEAL, spaceBefore=11, spaceAfter=5, keepWithNext=True
    )
    q_style = ParagraphStyle(
        'Question', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9, leading=12.2,
        textColor=DEEP_SLATE, spaceBefore=5, spaceAfter=2, keepWithNext=True
    )
    a_style = ParagraphStyle(
        'Answer', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.4, leading=11.5,
        textColor=DARK_CHARCOAL, spaceAfter=5
    )
    demo_style = ParagraphStyle(
        'DemoBox', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=8, leading=11,
        textColor=SUCCESS_GREEN
    )

    elements = []
    
    elements.append(Paragraph("THE HUNGRY HELM — VIVA VOCE DEFENSE & DEMONSTRATION GUIDE", title_style))
    elements.append(Paragraph("<b>Agile Software Development (CSET455) | Evaluator: Rashmi Rani | Student: Prikshit Sharma (S24CSEU1823)</b>", subtitle_style))
    elements.append(Paragraph(
        "<b>Live Jira Project:</b> <font color='#0052cc'><u>https://prikshittt777.atlassian.net</u></font> (Key: <b>THH</b>, Board ID: <b>167</b>, Dashboard ID: <b>10001</b>)<br/>"
        "This viva preparation guide equips you to defend every Agile principle and technical decision, linking each concept directly to your live Jira project issues (<code>THH-3</code> to <code>THH-22</code>) and running codebase.",
        ParagraphStyle('Intro', parent=a_style, fontName='Helvetica-Oblique', textColor=MUTED_GREY)
    ))
    elements.append(HRFlowable(width="100%", thickness=1, color=BORDER_LIGHT, spaceAfter=8))
    
    qas = [
        ("Part 1: Agile, Scrum & Requirements Engineering (Labs 1 & 2)", [
            ("Q1: Why Scrum instead of Kanban for The Hungry Helm?",
             "<b>Direct Answer:</b> The Hungry Helm is an iteration-driven product development project with clear time-boxed milestones (Sprints 1 to 4) and sequential technical dependencies (database seed -> auth -> ordering -> KDS). Scrum's sprint cadence and sprint goals provide delivery predictability. Kanban is better suited for continuous support streams like IT helpdesk ticketing (as in Lab 4)."),
            ("Q2: How do your User Stories meet the INVEST criteria?",
             "<b>Direct Answer:</b> Each of our 14 stories (<code>THH-9</code> to <code>THH-22</code>) is Independent, Negotiable, Valuable, Estimable, Small, and Testable. For example, <code>THH-16 (Server-Side Price Verification)</code> is Small (5 SP), Valuable to security, and Testable via BDD Given/When/Then criteria: <i>'Given a cart with tampered item price INR 1, when checkout is submitted, backend fetches DB price INR 180 and persists verified total.'</i>"),
            ("Q3: What is the difference between an Epic and a Story in your Jira project?",
             "<b>Direct Answer:</b> In our Jira project, an <b>Epic</b> represents a high-level strategic capability spanning multiple iterations (e.g. <code>THH-6: Cart Management & Tamper-Proof Order Placement</code>). A <b>User Story</b> is a granular vertical slice sized to fit comfortably in a sprint (e.g. <code>THH-15: Persistent Cart</code> = 5 SP, and <code>THH-16: Server Checkout</code> = 5 SP).")
        ]),
        ("Part 2: Estimation, Velocity Planning & MoSCoW (Labs 3, 5, 6)", [
            ("Q4: What was your agreed baseline anchor story, and why?",
             "<b>Direct Answer:</b> Our agreed baseline anchor is <code>THH-9: Multi-Outlet Seed & Campus Data Model</code>, sized at <b>3 Story Points</b>. It was chosen because seeding 5 campus stalls in Mongoose involves well-understood schema structures, standard JSON fixtures, and zero external integration risk. All other stories were sized relative to this 3-point anchor."),
            ("Q5: How did you allocate stories across your 4 Sprints?",
             "<b>Direct Answer:</b> We calibrated a team velocity of <b>20 Story Points per 2-week Sprint</b>. Across our 67 total points, we sequenced stories by dependencies: Sprint 140 (18 pts - Foundation), Sprint 141 (18 pts - Ordering), Sprint 142 (18 pts - KDS & Status), and Sprint 143 (13 pts - Hardening). No sprint exceeds the 20-point capacity."),
            ("Q6: How did you handle scope trade-offs using MoSCoW when deadlines tightened?",
             "<b>Direct Answer:</b> Rather than using critical-path crashing (unrealistic overtime) or fast-tracking (skipping QA), we applied <b>MoSCoW prioritization</b>. When simulating an accelerated deadline, non-essential features (Razorpay online payment, 8 pts, and FCM push notifications, 5 pts) were deferred to v1.1 (Won't Have v1.0), protecting the stability of our core ordering and KDS pipeline.")
        ]),
        ("Part 3: Custom Jira Workflows & Quality Gates (Lab 7)", [
            ("Q7: What custom workflow rules did you configure on project THH?",
             "<b>Direct Answer:</b> We configured the <code>THH_Software_Scrum_Workflow</code> with 5 statuses: <b>Backlog -> To Do -> In Progress -> In Review / QA -> Done</b>, plus a reverse defect loop from In Review back to In Progress.<br/>"
             "• <b>Condition:</b> Only project members (Prikshit Sharma) can execute status transitions.<br/>"
             "• <b>Validator:</b> The 'Approve & Done' transition requires the <code>Fix Version</code> (v1.0) and <code>Resolution</code> fields to be non-empty.<br/>"
             "• <b>Post-Function:</b> Automatically sets Resolution to 'Completed' and logs transition timestamps.")
        ]),
        ("Part 4: Real-World Architecture & Code Verification", [
            ("Q8: How does your application connect to MongoDB, and how did you solve connection dropouts?",
             "<b>Direct Answer:</b> In <code>backend/server.js</code>, we implemented an architectural fallback using <code>mongodb-memory-server</code>. When the server boots, it first attempts to connect to MongoDB Atlas. If network restrictions, captive portals, or firewall rules block Atlas, the catch block automatically boots an in-memory MongoDB instance and triggers <code>seedDatabase()</code> immediately. Evaluators can run the system anywhere with zero database setup."),
            ("Q9: How does the server prevent client-side price tampering during order placement?",
             "<b>Direct Answer:</b> In <code>backend/controllers/orderController.js</code> (linked to story <code>THH-16</code>), the server never trusts client-submitted prices. It takes the item IDs from the cart, queries the database for the canonical item prices, recalculates the subtotal and taxes on the server, and persists the verified amount. If a client intercepts the request and alters INR 180 to INR 1, the server overwrites it with INR 180."),
            ("Q10: Why did you shift the backend port from 5000 to 5001?",
             "<b>Direct Answer:</b> On macOS Sonoma and Sequoia, the native ControlCenter AirPlay Receiver service listens on port 5000 by default (<code>EADDRINUSE: :::5000</code>). In story <code>THH-20</code>, we configured <code>backend/.env</code> to <code>PORT=5001</code> and updated <code>frontend/script.js</code> to target port 5001, eliminating local port collisions.")
        ])
    ]
    
    for section_title, q_list in qas:
        elements.append(Paragraph(section_title, h1_style))
        for q, a in q_list:
            elements.append(Paragraph(q, q_style))
            elements.append(Paragraph(a, a_style))
        elements.append(Spacer(1, 4))
        
    # Live Demo Script
    elements.append(Paragraph("Part 5: Step-by-Step Live Demonstration Script for Faculty", h1_style))
    demo_steps = [
        ("Step 1: Open Live Jira Workspace", "Open <code>https://prikshittt777.atlassian.net/jira/software/c/projects/THH/boards/167/backlog</code>. Point out the 6 Epics (THH-3 to 8), 14 User Stories (THH-9 to 22), and 4 Sprints (140 to 143)."),
        ("Step 2: Show Active Scrum Board", "Click 'Board' (ID: 167). Show Sprint 140 active with THH-9 & THH-10 in Done, THH-11 in Progress, and THH-12 in To Do."),
        ("Step 3: Show Custom Dashboard", "Navigate to <code>https://prikshittt777.atlassian.net/jira/dashboards/10001</code>. Show the 4 configured gadgets: Sprint Burndown, Created vs Resolved, Filter Stats, and Sprint Health."),
        ("Step 4: Demonstrate Running Application", "Open <code>http://localhost:3000</code>. Log in as student (<code>prikshit@bennett.edu.in</code> / <code>password</code>). Show campus food chart with live badges. Add Kathi Roll to cart."),
        ("Step 5: Demonstrate Staff KDS", "Open <code>http://localhost:3000/kds.html</code> in incognito. Log in as staff (<code>IK-STAFF-001</code> / <code>staff123</code>). Advance order status from incoming -> preparing -> ready. Show student voyage log compass lighting up in real time.")
    ]
    for s, desc in demo_steps:
        elements.append(Paragraph(f"<b>{s}</b>", demo_style))
        elements.append(Paragraph(desc, a_style))
        
    doc.build(elements, canvasmaker=VivaNumberedCanvas)
    print(f"Successfully generated Viva Guide: {pdf_filename}")

if __name__ == "__main__":
    build_viva_guide()
