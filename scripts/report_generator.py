# scripts/report_generator.py
 
import json
 
data = json.load(open("reports/result.json"))
 
html = f"""
<h1>Resilience Report</h1>
<p>Application: {data['application']}</p>
<p>Score: {data['score']}</p>
"""
 
with open("reports/report.html","w") as f:
    f.write(html) 