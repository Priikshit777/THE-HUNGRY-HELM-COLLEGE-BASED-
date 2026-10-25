#!/usr/bin/env python3
"""
Generate Viva Defense Preparation Guide PDF for The Hungry Helm
Student: Prikshit Sharma | Enrollment: S24CSEU1823 | Course: CSET455
Faculty: Rashmi Rani | Bennett University
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

# Palette
TEAL = colors.HexColor("#1a5f5a")
DEEP_SLATE = colors.HexColor("#264653")
GOLD = colors.HexColor("#b8860b")
DARK_CHARCOAL = colors.HexColor("#172b4d")
MUTED_GREY = colors.HexColor("#5e6c84")
BG_LIGHT = colors.HexColor("#f4f5f7")
BORDER_LIGHT = colors.HexColor("#dfe1e6")
SUCCESS_GREEN = colors.HexColor("#006644")
SUCCESS_BG = colors.HexColor("#e3fcef")
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
        self.drawString(54, 34, "Student: Prikshit Sharma (S24CSEU1823)  •  Project: The Hungry Helm (THH)")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 54, 34, page_str)
        self.restoreState()

def build_viva_guide():
    pdf_filename = "Prikshit_Sharma_S24CSEU1823_Viva_Defense_Guide.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
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
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=TEAL,
        spaceBefore=12,
        spaceAfter=5,
        keepWithNext=True
    )
    
    q_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12.5,
        textColor=DEEP_SLATE,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )
    
    a_style = ParagraphStyle(
        'Answer',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.8,
        textColor=DARK_CHARCOAL,
        spaceAfter=6
    )
    
    code_inline_style = ParagraphStyle(
        'CodeInline',
        parent=a_style,
        fontName='Courier',
        fontSize=8,
        textColor=colors.HexColor("#0052cc")
    )

    demo_style = ParagraphStyle(
        'DemoBox',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=SUCCESS_GREEN
    )

    elements = []
    
    # Title Block
    elements.append(Paragraph("THE HUNGRY HELM — VIVA VOCE DEFENSE & DEMONSTRATION GUIDE", title_style))
    elements.append(Paragraph("<b>Agile Software Development (CSET455) | Evaluator: Rashmi Rani | Student: Prikshit Sharma (S24CSEU1823)</b>", subtitle_style))
    elements.append(Paragraph(
        "This cheat sheet prepares you for rapid-fire technical and conceptual questioning during tomorrow's evaluation. Every answer connects abstract Agile principles directly to your real Jira project (<b>THH</b>) and your live verified codebase (ports 5001 & 3000).",
        ParagraphStyle('Intro', parent=a_style, fontName='Helvetica-Oblique', textColor=MUTED_GREY)
    ))
    elements.append(HRFlowable(width="100%", thickness=1, color=BORDER_LIGHT, spaceAfter=8))
    
    # =========================================================================
    # PART 1: AGILE & SCRUM FUNDAMENTALS
    # =========================================================================
    elements.append(Paragraph("Part 1: Agile, Scrum & Requirements Engineering (Labs 1 & 2)", h1_style))
    
    qas_p1 = [
        ("Q1: Why did you choose Scrum over Kanban for The Hungry Helm?",
         "<b>Direct Answer:</b> The Hungry Helm is an iteration-driven product development effort with clear time-boxed milestones (Sprints 1 to 4) and cross-functional feature dependencies (auth, ordering, kitchen dispatch). Scrum's sprint planning, sprint goals, and fixed cadence provide the predictability needed for delivering a cohesive v1.0 release. Kanban is better suited for continuous support or IT helpdesk ticket streams (as in Lab 4)."),
        
        ("Q2: What is the INVEST criteria, and how do your User Stories meet it?",
         "<b>Direct Answer:</b> INVEST stands for <b>Independent, Negotiable, Valuable, Estimable, Small, and Testable</b>. In The Hungry Helm, each of the 14 stories is vertical and independently deliverable. For example, <code>THH-8 (Server-Side Price Verification)</code> is Small (5 SP), Valuable to security, and Testable via explicit Given/When/Then acceptance criteria: <i>'Given a cart with tampered item price ₹1, when checkout is submitted, backend fetches DB price ₹180 and calculates verified total.'</i>"),
        
        ("Q3: How do you distinguish an Epic from a User Story?",
         "<b>Direct Answer:</b> An <b>Epic</b> represents a substantial body of work or broad capability that cannot be completed within a single sprint and must be decomposed (e.g. <code>THH-E4: Cart Management & Tamper-Proof Order Placement</code>). A <b>User Story</b> is a thin, vertical slice of user value sized to fit comfortably within a two-week sprint (e.g. <code>THH-7: Persistent Cart</code> = 5 SP, and <code>THH-8: Server Checkout</code> = 5 SP)."),
        
        ("Q4: Why do you use Story Points and Fibonacci numbers instead of hours or days?",
         "<b>Direct Answer:</b> Estimating in hours falls victim to developer optimism, individual skill variations, and false precision. <b>Story Points</b> represent relative sizing—factoring in complexity, uncertainty, and effort. We use the modified Fibonacci sequence (1, 2, 3, 5, 8, 13) because uncertainty scales non-linearly; it is easier to agree whether a task is twice as hard as another than whether it takes 14 versus 16 hours.")
    ]
    for q, a in qas_p1:
        elements.append(Paragraph(q, q_style))
        elements.append(Paragraph(a, a_style))
        
    elements.append(Spacer(1, 6))

    # =========================================================================
    # PART 2: SPRINT PLANNING, VELOCITY & MOSCOW (LABS 3, 5, 6)
    # =========================================================================
    elements.append(Paragraph("Part 2: Estimation, Velocity Planning & MoSCoW Scope Trade-Offs (Labs 3, 5, 6)", h1_style))
    
    qas_p2 = [
        ("Q5: What was your agreed baseline anchor story, and why?",
         "<b>Direct Answer:</b> Our agreed baseline anchor is <code>THH-1: Multi-Outlet Seed & Campus Data Model</code>, sized at <b>3 Story Points</b>. It was chosen because seeding 5 campus stalls in Mongoose involves well-understood schema structures, standard JSON fixtures, and zero unknown external dependencies. Every other story was sized relative to this 3-point benchmark."),
        
        ("Q6: How did you calculate team capacity and plan your 4 Sprints?",
         "<b>Direct Answer:</b> We calibrated a team velocity of <b>20 Story Points per 2-week Sprint</b>. Across our 67 total points, we sequenced stories based on technical dependencies across 4 Sprints: Sprint 1 (18 pts - Core Platform), Sprint 2 (18 pts - Ordering & Security), Sprint 3 (18 pts - Kitchen Display), and Sprint 4 (13 pts - Hardening & Release). No sprint exceeded the 20-point limit."),
        
        ("Q7: How would you respond if the client advanced the launch date by one week?",
         "<b>Direct Answer:</b> In traditional Waterfall, project managers attempt 'crashing' (adding overtime) or 'fast-tracking' (running tasks in parallel), which introduces severe quality bugs. In Agile, we negotiate <b>Scope Trade-Offs using MoSCoW prioritization</b>. When simulating an accelerated deadline, we deferred non-essential features (Razorpay online payment, 8 pts, and FCM push notifications, 5 pts) into Phase 3 (Won't Have v1.0). This protected our core ordering and kitchen dispatch pipeline without compromising quality."),
        
        ("Q8: What is a Hardening Sprint, and why is Sprint 4 sized at 13 points instead of 20?",
         "<b>Direct Answer:</b> A <b>Hardening Sprint</b> (Lab 6 Task 4) is an iteration reserved purely for stabilization, end-to-end integration testing, performance verification, and security audits—no new feature stories are introduced. Sprint 4 was intentionally sized to 13 planned points (THH-12, THH-13, THH-14), leaving a 7-point contingency buffer (~35%) for addressing unexpected bugs discovered during pre-submission testing.")
    ]
    for q, a in qas_p2:
        elements.append(Paragraph(q, q_style))
        elements.append(Paragraph(a, a_style))

    elements.append(Spacer(1, 6))

    # =========================================================================
    # PART 3: JIRA WORKFLOWS & QUALITY GATES (LAB 7)
    # =========================================================================
    elements.append(Paragraph("Part 3: Custom Jira Workflows, Statuses & Quality Gates (Lab 7)", h1_style))
    
    qas_p3 = [
        ("Q9: What custom workflow statuses and rules did you configure in Jira?",
         "<b>Direct Answer:</b> We engineered the <code>THH_Software_Scrum_Workflow</code> with 5 distinct statuses: <b>Backlog → To Do → In Progress → In Review / QA → Done</b>, plus a reverse defect loop from In Review back to In Progress.<br/>"
         "We enforced three types of transition rules:<br/>"
         "• <b>Condition:</b> Only users in the 'Developers' or 'Administrators' project role can execute transitions.<br/>"
         "• <b>Validator:</b> On the 'Approve & Complete' transition, the fields <code>Resolution</code> and <code>Fix Version</code> (v1.0) must not be empty, and the linked GitHub PR must be merged.<br/>"
         "• <b>Post-Function:</b> Automatically sets Resolution to 'Completed' and fires an 'Issue Resolved' email event to the Project Lead."),
        
        ("Q10: What is the difference between a Condition, a Validator, and a Post-Function in Jira?",
         "<b>Direct Answer:</b><br/>"
         "• <b>Condition:</b> Evaluated <i>before</i> a user sees a transition button. If false, the button is completely hidden.<br/>"
         "• <b>Validator:</b> Checked <i>after</i> the user clicks the transition button and enters screen data. If validation fails, an error message appears and the issue does not move.<br/>"
         "• <b>Post-Function:</b> An automated system action executed <i>immediately after</i> a successful transition (e.g. setting fields, clearing assignees, sending webhooks).")
    ]
    for q, a in qas_p3:
        elements.append(Paragraph(q, q_style))
        elements.append(Paragraph(a, a_style))

    elements.append(Spacer(1, 6))

    # =========================================================================
    # PART 4: METRICS, CHARTS & DASHBOARDS (LABS 4, 6, 8)
    # =========================================================================
    elements.append(Paragraph("Part 4: Agile Metrics, Burndown, Burnup & Dashboards (Labs 4, 6, 8)", h1_style))
    
    qas_p4 = [
        ("Q11: How do you interpret a Sprint Burndown chart vs a Release Burnup chart?",
         "<b>Direct Answer:</b><br/>"
         "• <b>Sprint Burndown:</b> Plots <i>remaining Story Points against time (working days)</i> in a single sprint. If the line is above the guideline, the team is behind; if below, ahead. On Day 6 of our Sprint 2, an upward bump shows a +3 pt scope trade-off that was burned down by Day 9.<br/>"
         "• <b>Release Burnup:</b> Plots <i>completed points against total scope over multiple sprints</i> toward a release (v1.0). It clearly reveals whether delays are caused by slow delivery or expanding scope (scope creep)."),
        
        ("Q12: What does a Cumulative Flow Diagram (CFD) tell you about a team's workflow?",
         "<b>Direct Answer:</b> The CFD shows the cumulative count of issues in each status over time. Parallel bands with a steady upward slope indicate a stable, predictable process. A widening 'In Progress' band indicates multitasking bottlenecks and violating WIP limits. In Hungry Helm, our CFD shows an average Work-In-Progress of 2.1 stories, Lead Time of 4.2 days, and Cycle Time of 2.1 days."),
        
        ("Q13: What gadgets did you place on your Jira Agile Dashboard?",
         "<b>Direct Answer:</b> We placed 4 specialized gadgets: (1) <b>Sprint Burndown Gadget</b> for live iteration tracking, (2) <b>Created vs. Resolved Chart</b> showing 20 created and 20 resolved (100% resolution), (3) <b>Two-Dimensional Filter Statistics</b> cross-tabulating status vs priority, and (4) <b>Velocity Chart</b> showing commitments vs actual completions across all 4 sprints.")
    ]
    for q, a in qas_p4:
        elements.append(Paragraph(q, q_style))
        elements.append(Paragraph(a, a_style))

    elements.append(Spacer(1, 6))

    # =========================================================================
    # PART 5: HUNGRY HELM ARCHITECTURE & CODE VERIFICATION
    # =========================================================================
    elements.append(Paragraph("Part 5: Hungry Helm Full-Stack Architecture & Implementation", h1_style))
    
    qas_p5 = [
        ("Q14: How does your application connect to MongoDB, and how did you solve connection failures?",
         "<b>Direct Answer:</b> In <code>backend/server.js</code>, we engineered an architectural fallback using <code>mongodb-memory-server</code>. When the server boots, it first attempts to connect to MongoDB Atlas using <code>process.env.MONGO_URI</code>. If network restrictions, captive portals, or firewall rules block Atlas, the catch block automatically spins up a local in-memory MongoDB instance and triggers <code>seedDatabase()</code> immediately. This guarantees that evaluators can run the system anywhere with zero database configuration."),
        
        ("Q15: How does your server prevent client-side price tampering during order checkout?",
         "<b>Direct Answer:</b> In <code>backend/controllers/orderController.js</code>, the backend <b>never trusts prices sent in the client request body</b>. Instead, it extracts the <code>outletId</code> and <code>items[i].itemId</code>, queries the database source-of-truth for the canonical item prices, recalculates the subtotal, taxes, and grand total on the server, and persists the verified amount. If a malicious user intercepts the HTTP payload and edits ₹180 to ₹1, the server overwrites it with ₹180."),
        
        ("Q16: How is role-based authentication enforced between students and outlet staff?",
         "<b>Direct Answer:</b> In <code>backend/middleware/auth.js</code>, incoming requests pass through JWT verification. The token payload encodes the user's role (<code>student</code> vs <code>staff</code>) and for staff, their specific <code>outletId</code> (e.g. <code>ik</code> for Kathi Castle). When staff access the Kitchen Display System (<code>/api/orders/staff</code>), the controller enforces a query filter <code>{ outlet: req.user.outletId }</code>, strictly isolating each kitchen's tickets."),
        
        ("Q17: Why did you shift the backend port from 5000 to 5001?",
         "<b>Direct Answer:</b> On macOS (Sonoma/Sequoia), the native Control Center / AirPlay Receiver service listens on port 5000 by default (<code>EADDRINUSE: :::5000</code>). In <code>THH-12</code>, we updated <code>backend/.env</code> to <code>PORT=5001</code> and modified <code>frontend/script.js</code> to target <code>http://localhost:5001/api</code>, ensuring clean zero-conflict execution.")
    ]
    for q, a in qas_p5:
        elements.append(Paragraph(q, q_style))
        elements.append(Paragraph(a, a_style))

    elements.append(Spacer(1, 6))

    # =========================================================================
    # PART 6: LIVE VIVA DEMONSTRATION WALKTHROUGH
    # =========================================================================
    elements.append(Paragraph("Part 6: Step-by-Step Live Demonstration Script for Faculty", h1_style))
    
    demo_steps = [
        ("Step 1: Open Running Services",
         "Open browser tabs: Frontend at <code>http://localhost:3000</code> and Backend Health at <code>http://localhost:5001/api/health</code>. Show that both daemons are active and healthy."),
        
        ("Step 2: Demonstrate Student Authentication & Food Chart (THH-3, THH-5)",
         "Log in as <code>prikshit@bennett.edu.in</code> with password <code>password</code>. Point out the nautical campus chart displaying live operational badges ('Open', '15-20 min wait') for Kathi Castle, Southern Soul, etc."),
        
        ("Step 3: Demonstrate Cart & Single-Outlet Conflict Shield (THH-6, THH-7)",
         "Click 'Kathi Castle' → Add 'Paneer Kathi Roll' (₹180). Open cart. Then browse 'Southern Soul' and attempt to add 'Masala Dosa'—show the modal prompt explaining that orders cannot cross multiple kitchens."),
        
        ("Step 4: Demonstrate Tamper-Proof Order Placement (THH-8)",
         "Click Checkout. Show the console network tab: order #101 is created for ₹300 (₹180 + ₹120 mock additions) with server-calculated totals. Point out the Voyage Log displaying status 'incoming'."),
        
        ("Step 5: Demonstrate Staff Kitchen Display & State Machine (THH-9, THH-10)",
         "In a separate window/incognito, open <code>http://localhost:3000/kds.html</code>. Log in as <code>IK-STAFF-001</code> / <code>staff123</code>. Show order #101 appearing on the KDS board. Advance status: <code>incoming → preparing → ready</code>."),
        
        ("Step 6: Show Synchronized Student Voyage Log Update (THH-11)",
         "Switch back to the student tab. Demonstrate the animated compass timeline lighting up to 'Food is Ready for Pickup!'. Show how polling synchronized the state seamlessly."),
        
        ("Step 7: Show Jira Project & GitHub DoD (THH-14, Lab 6)",
         "Open Jira project <code>THH</code> on <code>prikshittt777.atlassian.net</code>. Show the 4 Sprints in the Backlog, the active Scrum board in Done status, the Custom Workflow in Project Settings, and the GitHub commit linkage in the Development panel.")
    ]
    for s, desc in demo_steps:
        elements.append(Paragraph(f"<b>{s}</b>", demo_style))
        elements.append(Paragraph(desc, a_style))

    # Build Document
    doc.build(elements, canvasmaker=VivaNumberedCanvas)
    print(f"Successfully generated Viva Defense Guide PDF: {pdf_filename}")

if __name__ == "__main__":
    build_viva_guide()
