import yaml
import json
 
# Load architecture
with open("architecture/application.yaml") as f:
    app_data = yaml.safe_load(f)
 
# Load policies
with open("policies/resilience_rules.yaml") as f:
    policy_data = yaml.safe_load(f)
 
max_score = policy_data["scoring"]["max_score"]
score = max_score
 
violations = []
 
for service in app_data["services"]:
 
    # Replicas
    if service.get("replicas", 1) < 2:
        score -= policy_data["policies"]["replicas"]["weight"]
        violations.append(
            f"{service['name']}: replicas less than 2"
        )
 
    # Health Check
    if not service.get("healthCheck", False):
        score -= policy_data["policies"]["health_check"]["weight"]
        violations.append(
            f"{service['name']}: health check missing"
        )
 
    # Resources
    if not service.get("resources", False):
        score -= policy_data["policies"]["resources"]["weight"]
        violations.append(
            f"{service['name']}: resource limits missing"
        )
 
    # Autoscaling
    if not service.get("autoscaling", False):
        score -= policy_data["policies"]["autoscaling"]["weight"]
        violations.append(
            f"{service['name']}: autoscaling disabled"
        )
 
    # PDB
    if not service.get("pdbEnabled", False):
        score -= policy_data["policies"]["pod_disruption_budget"]["weight"]
        violations.append(
            f"{service['name']}: PDB not configured"
        )
 
    # Chaos Testing
    if not service.get("chaosTested", False):
        score -= policy_data["policies"]["chaos_testing"]["weight"]
        violations.append(
            f"{service['name']}: chaos testing not executed"
        )
 
    # TLS
    if not service.get("tlsEnabled", False):
        score -= policy_data["policies"]["tls"]["weight"]
        violations.append(
            f"{service['name']}: TLS not enabled"
        )
 
    # Monitoring
    if not service.get("monitoring", False):
        score -= policy_data["policies"]["monitoring"]["weight"]
        violations.append(
            f"{service['name']}: monitoring missing"
        )
 
    # Logging
    if not service.get("logging", False):
        score -= policy_data["policies"]["logging"]["weight"]
        violations.append(
            f"{service['name']}: logging missing"
        )
 
    # Tracing
    if not service.get("tracing", False):
        score -= policy_data["policies"]["tracing"]["weight"]
        violations.append(
            f"{service['name']}: tracing missing"
        )
 
    # Circuit Breaker
    if not service.get("circuitBreaker", False):
        score -= policy_data["policies"]["circuit_breaker"]["weight"]
        violations.append(
            f"{service['name']}: circuit breaker not configured"
        )
 
    # Database Backup
    if service["name"] == "database":
        if not service.get("backupEnabled", False):
            score -= policy_data["policies"]["backup"]["weight"]
            violations.append(
                "database: backup not enabled"
            )
 
    # Retry Policy
    if not service.get("retryPolicy", False):
        score -= 5
 
    # Bulkhead
    if not service.get("bulkhead", False):
        score -= 10
 
    # Timeout Policy    
    if not service.get("timeoutPolicy", False):
        score -= 5
 
    # Rate Limiting
    if not service.get("rateLimiting", False):
        score -= 5
 
    # Prevent negative scores
    if score < 0:
        score = 0
 
# Determine status
passing_score = policy_data["scoring"]["passing_score"]
warning_score = policy_data["scoring"]["warning_score"]
 
if score >= passing_score:
    status = "PASS"
elif score >= warning_score:
    status = "WARNING"
else:
    status = "FAIL"
 
result = {
    "application": app_data["application"]["name"],
    "score": score,
    "status": status,
    "violations": violations
}
 
with open("reports/result.json", "w") as f:
    json.dump(result, f, indent=2)
 
print(json.dumps(result, indent=2))