import os
import json
import requests
 
# JIRA_URL = os.environ["JIRA_URL"]
# JIRA_EMAIL = os.environ["JIRA_EMAIL"]
# JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
 
JIRA_URL="https://swamypte.atlassian.net/"
JIRA_EMAIL="swamy.pte@gmail.com"
JIRA_API_TOKEN="ATATT3xFfGF0XpOV67MqjnQSLx5qIysNQe5vZNArAkPV3QPWb98kYo0pSHSw_ERFJkjPN7yi4rOd6xU6sbAFBcoAX6RTQwn3m2M2Arn_CZHzRCdoHMCBIG05qiUiiuolPpRg2c99Wz2iTapLQhhmiLzS90LE2r42UO9KYpU4fKSYbIG5qQCnXf4=8F1891EC"
payload = {
    "fields": {
        "project": {
            "key": "SCRUM"
        },
        "summary": "Harness Resilience Assessment Failed",
        "issuetype": {
            "name": "Task"
        }
    }
}
 
# Create Jira Issue
response = requests.post(
    f"{JIRA_URL}/rest/api/3/issue",
    auth=(JIRA_EMAIL, JIRA_API_TOKEN),
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    data=json.dumps(payload)
)
 
print(response.text)
 
# Check if issue creation succeeded
if response.status_code in [200, 201]:
    issue_key = response.json()["key"]
    print(f"Created Jira Issue: {issue_key}")
 
    # Attach report file
    report_path = "reports/report.html"
 
    if os.path.exists(report_path):
        with open(report_path, "rb") as f:
            attach_response = requests.post(
                f"{JIRA_URL}/rest/api/3/issue/{issue_key}/attachments",
                auth=(JIRA_EMAIL, JIRA_API_TOKEN),
                headers={
                    "X-Atlassian-Token": "no-check"
                },
                files={
                    "file": (
                        "report.html",
                        f,
                        "text/html"
                    )
                }
            )
 
        print("Attachment Status:", attach_response.status_code)
        print(attach_response.text)
    else:
        print("report.html not found")
else:
    print("Failed to create Jira issue")
