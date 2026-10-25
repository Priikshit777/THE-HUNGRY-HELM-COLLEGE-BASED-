#!/usr/bin/env python3
"""
Create 4 Sprints with names < 30 chars on Board 167 and assign issues to them.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

SITE_URL = "https://prikshittt777.atlassian.net"
EMAIL = "prikshittt777@gmail.com"
BOARD_ID = 167

token = None
with open("backend/.env", "r") as f:
    for line in f:
        if line.startswith("JIRA_API_TOKEN="):
            token = line.split("=", 1)[1].strip()

auth = HTTPBasicAuth(EMAIL, token)

sprints = [
    {
        "name": "THH Sprint 1 - Foundation",
        "goal": "Deliver multi-outlet seed models, resilient in-memory DB fallback, and student/staff JWT authentication.",
        "startDate": "2026-10-12T09:00:00.000+05:30",
        "endDate": "2026-10-25T18:00:00.000+05:30",
        "issues": ["THH-9", "THH-10", "THH-11", "THH-12"]
    },
    {
        "name": "THH Sprint 2 - Ordering",
        "goal": "Build interactive campus food chart, single-outlet persistent cart, and tamper-proof server price checkout.",
        "startDate": "2026-10-26T09:00:00.000+05:30",
        "endDate": "2026-11-08T18:00:00.000+05:30",
        "issues": ["THH-13", "THH-14", "THH-15", "THH-16"]
    },
    {
        "name": "THH Sprint 3 - KDS & Status",
        "goal": "Implement staff kitchen display board and synchronized 4-stage order pipeline with live voyage tracking.",
        "startDate": "2026-11-09T09:00:00.000+05:30",
        "endDate": "2026-11-22T18:00:00.000+05:30",
        "issues": ["THH-17", "THH-18", "THH-19"]
    },
    {
        "name": "THH Sprint 4 - Hardening",
        "goal": "Resolve port collisions, execute automated E2E test suites, and perform production security audit.",
        "startDate": "2026-11-23T09:00:00.000+05:30",
        "endDate": "2026-12-06T18:00:00.000+05:30",
        "issues": ["THH-20", "THH-21", "THH-22"]
    }
]

for s in sprints:
    payload = {
        "name": s["name"],
        "goal": s["goal"],
        "startDate": s["startDate"],
        "endDate": s["endDate"],
        "originBoardId": BOARD_ID
    }
    res = requests.post(f"{SITE_URL}/rest/agile/1.0/sprint", json=payload, auth=auth)
    if res.status_code in [200, 201]:
        sprint_id = res.json()["id"]
        print(f"✔ Created Sprint: ID {sprint_id} -> {s['name']}")
        # Move issues into this sprint
        m_res = requests.post(f"{SITE_URL}/rest/agile/1.0/sprint/{sprint_id}/issue", json={"issues": s["issues"]}, auth=auth)
        if m_res.status_code == 204:
            print(f"  ✔ Moved {len(s['issues'])} issues into Sprint ID {sprint_id}: {', '.join(s['issues'])}")
        else:
            print(f"  ✖ Failed to move issues: {m_res.status_code} {m_res.text}")
    else:
        print(f"✖ Failed to create Sprint {s['name']}: {res.status_code} {res.text}")
