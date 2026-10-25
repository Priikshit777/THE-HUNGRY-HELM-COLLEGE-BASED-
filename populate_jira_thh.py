#!/usr/bin/env python3
"""
Populate Jira Cloud with complete The Hungry Helm (THH) Scrum Architecture.
Creates:
- 6 Epics
- 14 User Stories with BDD acceptance criteria & Fibonacci story points
- 4 Sprints with sprint goals & capacity
- Moves stories into their respective sprints
"""

import os
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

SITE_URL = "https://prikshittt777.atlassian.net"
EMAIL = "prikshittt777@gmail.com"

# Read token safely from backend/.env
token = None
with open("backend/.env", "r") as f:
    for line in f:
        if line.startswith("JIRA_API_TOKEN="):
            token = line.split("=", 1)[1].strip()

if not token:
    print("Error: JIRA_API_TOKEN not found in backend/.env")
    sys.exit(1)

auth = HTTPBasicAuth(EMAIL, token)

def make_adf_description(desc_text, criteria_list):
    """Generate Atlassian Document Format (ADF) description with paragraphs and bullet list."""
    content = [
        {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "text": desc_text
                }
            ]
        },
        {
            "type": "heading",
            "attrs": {"level": 3},
            "content": [
                {
                    "type": "text",
                    "text": "Acceptance Criteria (BDD Given/When/Then)"
                }
            ]
        }
    ]
    
    bullet_items = []
    for crit in criteria_list:
        bullet_items.append({
            "type": "listItem",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": crit
                        }
                    ]
                }
            ]
        })
        
    content.append({
        "type": "bulletList",
        "content": bullet_items
    })
    
    return {
        "type": "doc",
        "version": 1,
        "content": content
    }

# 1. Epics Definition
epics_data = [
    {
        "name": "Platform Foundation",
        "summary": "Core Platform Architecture & Multi-Outlet Foundation",
        "desc": "Establish foundational RESTful API, database schemas, seed configurations, and outlet domain models for campus food stalls.",
        "criteria": [
            "Given system boot, REST API binds cleanly and verifies database connectivity.",
            "Database models enforce schema consistency for outlets, items, and orders.",
            "Environment configuration dynamically switches between Atlas and fallback modes."
        ]
    },
    {
        "name": "Campus Auth",
        "summary": "Student Identity & Secure Campus Authentication",
        "desc": "Implement role-based JWT authentication separating student patrons from outlet staff with password hashing and session tokens.",
        "criteria": [
            "Given student login, returns signed JWT token with student ID.",
            "Given staff login with badge, returns staff-scoped JWT with outletId.",
            "Passwords hashed using bcrypt before database persistence."
        ]
    },
    {
        "name": "Food Chart & Menus",
        "summary": "Dynamic Food Chart & Outlet Browsing Experience",
        "desc": "Deliver interactive visual campus food chart with outlet cards, live operational status, operating hours, and categorized menu browsing.",
        "criteria": [
            "Student dashboard renders campus food chart with live operational badges.",
            "Clicking an outlet opens modal displaying categorized menu items.",
            "Item thumbnails, INR prices, and dietary indicators (Veg/Non-Veg) displayed."
        ]
    },
    {
        "name": "Cart & Checkout",
        "summary": "Cart Management & Tamper-Proof Order Placement",
        "desc": "Build responsive shopping cart with single-outlet conflict prevention and server-side cryptographic price verification at checkout.",
        "criteria": [
            "Cart state persists in localStorage across browser reloads.",
            "Cross-outlet conflict shield triggers confirmation modal before switching stalls.",
            "Backend recalculates item totals from database to prevent price tampering."
        ]
    },
    {
        "name": "Kitchen Display System",
        "summary": "Real-Time Kitchen Display & Order Pipeline (KDS)",
        "desc": "Empower outlet kitchen staff with a dedicated KDS dashboard to track incoming tickets and transition order states smoothly.",
        "criteria": [
            "Staff KDS dashboard displays incoming tickets filtered by stall outletId.",
            "4-stage order pipeline advances: incoming -> preparing -> ready -> completed.",
            "Disallowed state transitions return HTTP 400 Bad Request."
        ]
    },
    {
        "name": "Hardening & Tracking",
        "summary": "Delivery Tracking, Voyage History & Production Hardening",
        "desc": "Provide student voyage order tracking, automated integration tests, runtime resilience fallbacks, and production security hardening.",
        "criteria": [
            "Student Voyage Log polls and displays animated compass timeline for order progress.",
            "Backend detects macOS AirPlay port 5000 collisions and shifts cleanly to port 5001.",
            "Automated integration test verifies full order lifecycle end-to-end.",
            "Security audit passes with Helmet headers, CORS policies, and sanitized error responses."
        ]
    }
]

# 2. User Stories Definition
stories_data = [
    # Sprint 1 (Platform Foundation)
    {
        "summary": "Multi-Outlet Seed & Campus Data Model",
        "epic_idx": 0,
        "points": 3,
        "priority": "High",
        "desc": "As a platform administrator, I want to seed standardized Bennett University outlet metadata (IK, HC, SS, SN, HS) so that all menus, operating hours, and stall locations are consistently modeled.",
        "criteria": [
            "Given database boot, when seed script runs, 5 campus outlets are populated with valid IDs, names, and menu items.",
            "Given existing records, seeding performs an idempotent upsert without duplicating documents.",
            "Each outlet record contains operational status (open/closed) and average wait times."
        ],
        "sprint_idx": 0
    },
    {
        "summary": "Resilient In-Memory & Production MongoDB Connection Layer",
        "epic_idx": 0,
        "points": 5,
        "priority": "Highest",
        "desc": "As a backend engineer, I want a dual-mode database connection architecture that automatically boots an in-memory MongoDB instance if the external Atlas cluster is unreachable, so that local development and academic evaluation never fail.",
        "criteria": [
            "Given an unreachable MONGO_URI, server catches error and initializes MongoMemoryServer transparently.",
            "Database seeding executes automatically upon fallback initialization.",
            "Application logs clearly indicate whether Atlas or In-Memory storage is active."
        ],
        "sprint_idx": 0
    },
    {
        "summary": "Bennett University Student JWT Authentication",
        "epic_idx": 1,
        "points": 5,
        "priority": "Highest",
        "desc": "As a Bennett University student, I want to authenticate using my campus email and password so that I receive a secure JWT bearer token to access authorized food ordering features.",
        "criteria": [
            "Given valid student credentials (prikshit@bennett.edu.in), system returns a signed JWT containing student ID and role.",
            "Given invalid credentials, system returns HTTP 401 Unauthorized with clean error payload.",
            "Passwords hashed using bcrypt before database persistence."
        ],
        "sprint_idx": 0
    },
    {
        "summary": "Outlet Staff Credential Verification & Role Isolation",
        "epic_idx": 1,
        "points": 5,
        "priority": "High",
        "desc": "As an outlet kitchen operator, I want to log in using my staff badge ID (e.g. IK-STAFF-001) so that I receive a staff-scoped JWT token restricting my view strictly to my stall's live kitchen orders.",
        "criteria": [
            "Given staff badge and password, system validates credentials and embeds outletId into JWT payload.",
            "Staff token cannot access or manipulate orders belonging to other outlets.",
            "Staff token cannot place customer orders."
        ],
        "sprint_idx": 0
    },

    # Sprint 2 (Ordering Experience & Security)
    {
        "summary": "Interactive Campus Food Chart Outlet Discovery",
        "epic_idx": 2,
        "points": 5,
        "priority": "High",
        "desc": "As a student explorer, I want to view a visual nautical chart of campus dining stalls with real-time operational badges and estimated preparation times so that I can decide where to eat.",
        "criteria": [
            "Given student dashboard loads, outlet cards for Kathi Castle, Southern Soul, Chai & More render dynamically.",
            "Outlets display live Open/Closed badges, operating hours, and average wait time.",
            "Clicking an outlet card triggers the detailed menu modal."
        ],
        "sprint_idx": 1
    },
    {
        "summary": "Categorized Outlet Menu Modal & Item Browsing",
        "epic_idx": 2,
        "points": 3,
        "priority": "Medium",
        "desc": "As a hungry patron, I want to browse items within an outlet categorized into Beverages, Quick Bites, and Meals with prices and dietary badges (Veg/Non-Veg) so that I can easily select items.",
        "criteria": [
            "Given an outlet is selected, modal displays all active menu items grouped by category.",
            "Each item displays thumbnail, name, description, price in INR, and dietary indicator.",
            "Add to Cart button increases item count with immediate visual feedback."
        ],
        "sprint_idx": 1
    },
    {
        "summary": "LocalStorage Persistent Cart & Cross-Outlet Conflict Prevention",
        "epic_idx": 3,
        "points": 5,
        "priority": "High",
        "desc": "As a student ordering food, I want my cart to persist across page refreshes and prevent mixing items from different outlets so that kitchen dispatch remains clean and manageable.",
        "criteria": [
            "Cart state persists in localStorage across browser reloads.",
            "Attempting to add an item from Outlet B while Cart contains items from Outlet A prompts clear-cart confirmation modal.",
            "Increment, decrement, and item removal dynamically update subtotal, tax, and order total."
        ],
        "sprint_idx": 1
    },
    {
        "summary": "Cryptographically Verified Server-Side Order Checkout",
        "epic_idx": 3,
        "points": 5,
        "priority": "Highest",
        "desc": "As a security-conscious engineer, I want the backend to re-calculate item prices from database source-of-truth during checkout rather than trusting client-submitted prices, preventing client-side price tampering exploits.",
        "criteria": [
            "Given checkout payload with altered item prices (e.g. ₹1 instead of ₹180), backend queries DB price and writes canonical amount.",
            "Backend verifies student JWT token and links order to student ID.",
            "Order record created with status 'incoming', unique Order ID (#101), and initial voyage log."
        ],
        "sprint_idx": 1
    },

    # Sprint 3 (Kitchen Display & Live Tracking)
    {
        "summary": "Real-Time Kitchen Display System (KDS) for Outlet Staff",
        "epic_idx": 4,
        "points": 8,
        "priority": "Highest",
        "desc": "As an outlet cook, I want a dedicated Kanban-style kitchen display showing active tickets organized by status so that my crew can prioritize food preparation during peak campus rush hours.",
        "criteria": [
            "Given staff logs into KDS, only tickets matching the authenticated staff outletId are rendered.",
            "Tickets display customer name, ordered items, quantity, special instructions, and elapsed timer.",
            "Visual alerts trigger for orders waiting longer than 15 minutes."
        ],
        "sprint_idx": 2
    },
    {
        "summary": "4-Stage Order Pipeline State Machine Transitions",
        "epic_idx": 4,
        "points": 5,
        "priority": "High",
        "desc": "As kitchen staff, I want to advance order status sequentially through incoming -> preparing -> ready -> completed via secure API endpoints so that both staff and students stay synchronized.",
        "criteria": [
            "PATCH /api/orders/:id/status endpoint enforces valid sequential state transitions.",
            "Disallowed state skips (e.g. incoming -> completed) return HTTP 400 Bad Request.",
            "Timestamps are recorded for each transition milestone."
        ],
        "sprint_idx": 2
    },
    {
        "summary": "Student Voyage Log & Live Order Status Polling",
        "epic_idx": 5,
        "points": 5,
        "priority": "High",
        "desc": "As a student waiting for lunch, I want a live Voyage Log displaying an animated compass timeline reflecting my order's current stage so that I know exactly when to walk to the outlet counter.",
        "criteria": [
            "Student order tracking screen fetches order updates via polling.",
            "Active stage lights up on nautical milestone tracker (Docked -> Cooking -> Ready -> Picked Up).",
            "Notification badge sounds or alerts when order moves to 'ready'."
        ],
        "sprint_idx": 2
    },

    # Sprint 4 (Hardening, Quality & Production Release)
    {
        "summary": "Port Conflict Resolution & Dynamic Local Environment Switching",
        "epic_idx": 5,
        "points": 3,
        "priority": "Medium",
        "desc": "As a DevOps engineer, I want the system to dynamically bind to port 5001 when macOS ControlCenter AirPlay occupies port 5000 and update frontend API baseUrl automatically, ensuring zero runtime initialization collisions.",
        "criteria": [
            "Environment variable PORT=5001 respected in backend config.",
            "Frontend script.js detects window.location or environment config to route API calls to active port.",
            "Health check endpoint GET /api/health responds with HTTP 200 and uptime metrics."
        ],
        "sprint_idx": 3
    },
    {
        "summary": "End-to-End Integration Test Suite & Automated Verification",
        "epic_idx": 5,
        "points": 5,
        "priority": "High",
        "desc": "As a QA test engineer, I want an automated end-to-end integration test script that verifies student auth, outlet browsing, tamper-proof order creation, staff order transition, and voyage log delivery in a single pipeline run.",
        "criteria": [
            "Test suite executes all 5 core stages against running backend.",
            "Exit code 0 returned on 100% test pass; non-zero on failure.",
            "Detailed assertions verify payload types, JWT claims, and price calculations."
        ],
        "sprint_idx": 3
    },
    {
        "summary": "Production Hardening, CORS & Helmet Security Audit",
        "epic_idx": 5,
        "points": 5,
        "priority": "High",
        "desc": "As a security auditor, I want to sanitize HTTP headers, configure CORS domain whitelisting, and implement error masking so that no stack traces or MongoDB connection strings are exposed in API error payloads.",
        "criteria": [
            "Helmet middleware attached to Express application.",
            "CORS configured with explicit allowed origins.",
            "Generic 500 Internal Server Error returned to clients with internal logging."
        ],
        "sprint_idx": 3
    }
]

# 3. Sprints Definition
sprints_meta = [
    {
        "name": "THH Sprint 1 - Core Platform Foundation",
        "goal": "Deliver multi-outlet seed models, resilient in-memory DB fallback, and student/staff JWT authentication.",
        "startDate": "2026-10-12T09:00:00.000+05:30",
        "endDate": "2026-10-25T18:00:00.000+05:30"
    },
    {
        "name": "THH Sprint 2 - Ordering Experience & Security",
        "goal": "Build interactive campus food chart, single-outlet persistent cart, and tamper-proof server price checkout.",
        "startDate": "2026-10-26T09:00:00.000+05:30",
        "endDate": "2026-11-08T18:00:00.000+05:30"
    },
    {
        "name": "THH Sprint 3 - Kitchen Display & Live Tracking",
        "goal": "Implement staff kitchen display board and synchronized 4-stage order pipeline with live voyage tracking.",
        "startDate": "2026-11-09T09:00:00.000+05:30",
        "endDate": "2026-11-22T18:00:00.000+05:30"
    },
    {
        "name": "THH Sprint 4 - Hardening, Quality & Production Release",
        "goal": "Resolve port collisions, execute automated E2E test suites, and perform production security audit.",
        "startDate": "2026-11-23T09:00:00.000+05:30",
        "endDate": "2026-12-06T18:00:00.000+05:30"
    }
]

def main():
    print("=== STARTING THE HUNGRY HELM JIRA POPULATION ===")
    
    # Step 1: Create Epics
    print("\n--- 1. Creating 6 Epics ---")
    created_epics = []
    for e in epics_data:
        payload = {
            "fields": {
                "project": {"key": "THH"},
                "issuetype": {"id": "10000"}, # Epic
                "summary": e["summary"],
                "description": make_adf_description(e["desc"], e["criteria"]),
                "customfield_10011": e["name"], # Epic Name
                "labels": ["epic", "hungry-helm", "cset455"]
            }
        }
        res = requests.post(f"{SITE_URL}/rest/api/3/issue", json=payload, auth=auth)
        if res.status_code in [200, 201]:
            data = res.json()
            created_epics.append(data["key"])
            print(f"✔ Created Epic: {data['key']} -> {e['name']} ({e['summary'][:40]}...)")
        else:
            print(f"✖ Failed to create Epic {e['name']}: {res.status_code} {res.text}")
            created_epics.append(None)
            
    # Step 2: Create User Stories
    print("\n--- 2. Creating 14 User Stories ---")
    created_stories = []
    for s in stories_data:
        epic_key = created_epics[s["epic_idx"]]
        payload = {
            "fields": {
                "project": {"key": "THH"},
                "issuetype": {"id": "10005"}, # Story
                "summary": s["summary"],
                "description": make_adf_description(s["desc"], s["criteria"]),
                "customfield_10016": float(s["points"]), # Story Points
                "priority": {"name": s["priority"]},
                "labels": ["user-story", "hungry-helm", f"sprint{s['sprint_idx']+1}"]
            }
        }
        if epic_key:
            payload["fields"]["customfield_10014"] = epic_key # Epic Link
            
        res = requests.post(f"{SITE_URL}/rest/api/3/issue", json=payload, auth=auth)
        if res.status_code in [200, 201]:
            data = res.json()
            created_stories.append({"key": data["key"], "sprint_idx": s["sprint_idx"], "points": s["points"]})
            print(f"✔ Created Story: {data['key']} ({s['points']} SP, {s['priority']}) -> {s['summary']}")
        else:
            print(f"✖ Failed to create story {s['summary']}: {res.status_code} {res.text}")
            
    # Step 3: Create 4 Sprints on Board 167
    print("\n--- 3. Creating 4 Sprints on Board 167 ---")
    board_id = 167
    created_sprints = []
    for sp in sprints_meta:
        payload = {
            "name": sp["name"],
            "goal": sp["goal"],
            "startDate": sp["startDate"],
            "endDate": sp["endDate"],
            "originBoardId": board_id
        }
        res = requests.post(f"{SITE_URL}/rest/agile/1.0/sprint", json=payload, auth=auth)
        if res.status_code in [200, 201]:
            data = res.json()
            created_sprints.append(data["id"])
            print(f"✔ Created Sprint: ID {data['id']} -> {sp['name']}")
        else:
            print(f"✖ Failed to create sprint {sp['name']}: {res.status_code} {res.text}")
            created_sprints.append(None)
            
    # Step 4: Move Stories into Sprints
    print("\n--- 4. Assigning Stories to Sprints ---")
    for s_idx, sprint_id in enumerate(created_sprints):
        if not sprint_id:
            continue
        issues_for_sprint = [st["key"] for st in created_stories if st["sprint_idx"] == s_idx]
        if issues_for_sprint:
            payload = {"issues": issues_for_sprint}
            res = requests.post(f"{SITE_URL}/rest/agile/1.0/sprint/{sprint_id}/issue", json=payload, auth=auth)
            if res.status_code == 204:
                print(f"✔ Moved {len(issues_for_sprint)} issues to Sprint {s_idx+1} (ID {sprint_id}): {', '.join(issues_for_sprint)}")
            else:
                print(f"✖ Failed to move issues to Sprint {s_idx+1}: {res.status_code} {res.text}")

    print("\n=== THE HUNGRY HELM JIRA POPULATION COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
