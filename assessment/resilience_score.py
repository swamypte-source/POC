class ResilienceScorer:
 
    @staticmethod
    def calculate(metrics):
 
        total = len(metrics)
 
        success = len(
            [m for m in metrics if m["status"] == 200]
        )
 
        availability = round(
            (success / total) * 100,
            2
        )
 
        avg_latency = round(
            sum(
                m["latency"] for m in metrics
            ) / total,
            2
        )
 
        latency_score = max(
            0,
            100 - (avg_latency / 10)
        )
 
        recovery_score = 95
 
        resilience_score = round(
            (
                availability * 0.5 +
                latency_score * 0.3 +
                recovery_score * 0.2
            ),
            2
        )
 
        return {
            "availability": availability,
            "avg_latency": avg_latency,
            "recovery_score": recovery_score,
            "resilience_score": resilience_score
        }