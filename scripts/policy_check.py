import os
import subprocess
import yaml
import json
import sys
 
with open("policies/resilience_rules.yaml") as f:
    policy = yaml.safe_load(f)
 
with open("reports/result.json") as f:
    result = json.load(f)
 
required_score = policy["scoring"]["passing_score"]
 
actual_score = result["score"]
 
print(f"Required Score : {required_score}")
print(f"Actual Score : {actual_score}")
 
if actual_score < required_score:
    print("FAIL - Deployment Blocked")
    print("Current Directory:", os.getcwd())
    print("Scripts Folder:", os.listdir("reports"))
    # subprocess.run([
    #     "python",
    #     "scripts/send_mail.py",
    #     str(actual_score),
    #     "FAIL"
    # ])
 
    subprocess.run([
        "python", "scripts/create_jira_bug.py"],
        check=True
    )
   
    sys.exit(1)
 
print("PASSED: Deployment Approved")