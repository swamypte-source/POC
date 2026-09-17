import requests
import time
 
 
class MetricsCollector:
 
    def __init__(self, target_url):
        self.target_url = target_url
 
    def collect(self, samples=30):
 
        result = []
 
        for _ in range(samples):
 
            start = time.time()
 
            try:
                response = requests.get(
                    self.target_url,
                    timeout=3
                )
 
                latency = round(
                    (time.time() - start) * 1000,
                    2
                )
 
                result.append({
                    "status": response.status_code,
                    "latency": latency
                })
 
            except Exception:
 
                result.append({
                    "status": 500,
                    "latency": 9999
                })
 
            time.sleep(1)
 
        return result