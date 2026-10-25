#!/usr/bin/env python3
"""
Automated Jira Cloud Setup Script for The Hungry Helm (THH)
Uses Jira REST API v3 & Agile API v1.0
Email: prikshittt777@gmail.com
"""

import sys
import os
import json
import requests
from requests.auth import HTTPBasicAuth

SITE_URL = "https://prikshittt777.atlassian.net"
EMAIL = "prikshittt777@gmail.com"

def get_auth(api_token):
    return HTTPBasicAuth(EMAIL, api_token)

def test_connection(auth):
    url = f"{SITE_URL}/rest/api/3/myself"
    res = requests.get(url, auth=auth)
    if res.status_code == 200:
        data = res.json()
        print(f"✔ Successfully authenticated as: {data.get('displayName')} ({data.get('emailAddress')})")
        return data.get('accountId')
    else:
        print(f"✖ Authentication failed ({res.status_code}): {res.text}")
        return None

def list_projects(auth):
    url = f"{SITE_URL}/rest/api/3/project"
    res = requests.get(url, auth=auth)
    if res.status_code == 200:
        return res.json()
    return []

def get_or_create_project(auth, lead_account_id):
    projects = list_projects(auth)
    for p in projects:
        if p.get("key") == "THH":
            print(f"✔ Found existing project: {p.get('name')} (Key: THH, ID: {p.get('id')})")
            return p
            
    print("Project THH does not exist. Creating Scrum project 'The Hungry Helm'...")
    # First get available project templates / types
    url = f"{SITE_URL}/rest/api/3/project"
    payload = {
        "key": "THH",
        "name": "The Hungry Helm",
        "projectTypeKey": "software",
        "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic",
        "description": "Campus Food Ordering Experience for Bennett University - Agile Software Development (CSET455)",
        "leadAccountId": lead_account_id,
        "assigneeType": "PROJECT_LEAD"
    }
    res = requests.post(url, json=payload, auth=auth)
    if res.status_code in [200, 201]:
        data = res.json()
        print(f"✔ Successfully created project: The Hungry Helm (Key: THH, ID: {data.get('id')})")
        return data
    else:
        print(f"Note: Standard template creation returned {res.status_code}: {res.text}")
        # Try software simplified template
        payload["projectTemplateKey"] = "com.pyxis.greenhopper.jira:basic-software-development-template"
        res2 = requests.post(url, json=payload, auth=auth)
        if res2.status_code in [200, 201]:
            print(f"✔ Successfully created project: The Hungry Helm (Key: THH)")
            return res2.json()
        else:
            print(f"Error creating project: {res2.text}")
            return None

def get_project_issue_types(auth, project_id_or_key):
    url = f"{SITE_URL}/rest/api/3/issuetype/project?projectId={project_id_or_key}"
    res = requests.get(url, auth=auth)
    if res.status_code == 200:
        types = res.json()
        type_map = {}
        for t in types:
            type_map[t.get("name").lower()] = t.get("id")
        return type_map
    return {}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 jira_api_setup.py <ATLASSIAN_API_TOKEN>")
        sys.exit(1)
        
    token = sys.argv[1].strip()
    auth = get_auth(token)
    account_id = test_connection(auth)
    if not account_id:
        sys.exit(1)
        
    project = get_or_create_project(auth, account_id)
    print(f"Project state: {project}")
