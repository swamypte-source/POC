import json
 
 
class ReportGenerator:
 
    @staticmethod
    def generate(result):
 
        with open(
            "reports/results.json",
            "w"
        ) as file:
            json.dump(
                result,
                file,
                indent=4
            )
 
        html_content = f"""
        <html>
        <head>
            <title>Resilience Report</title>
        </head>
        <body>
            <h1>Resilience Assessment Report</h1>
            <p>Availability : {result['availability']}%</p>
            <p>Average Latency : {result['avg_latency']} ms</p>
            <p>Recovery Score : {result['recovery_score']}</p>
            <p>Resilience Score : {result['resilience_score']}</p>
        </body>
        </html>
        """
 
        with open(
            "reports/report.html",
            "w"
        ) as file:
            file.write(html_content)