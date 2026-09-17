import smtplib
import sys
from email.message import EmailMessage
from pathlib import Path
 
score = sys.argv[1]
status = sys.argv[2]
 
sender = "swamy.pte@gmail.com"
app_password = "ykab arbo tpiu vmdu"
 
receiver = "swamy.pte@gmail.com"
 
msg = EmailMessage()
 
msg["Subject"] = f"Harness Pipeline {status}"
msg["From"] = sender
msg["To"] = receiver
 
msg.set_content(f"""
Pipeline Status : {status}
 
Resilience Score : {score}
 
Please review the attached resilience report.
""")
 
# Attach HTML report
report_file = Path("reports/report.html")
 
if report_file.exists():
    with open(report_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="html",
            filename="report.html"
        )
else:
    print("WARNING: report.html not found")
 
with smtplib.SMTP("smtp.gmail.com", 587,timeout=30) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender, app_password)
    smtp.send_message(msg)
 
print("Email sent successfully")