import subprocess
 
 
class ExperimentManager:
 
    @staticmethod
    def run_pod_delete():
 
        subprocess.run([
            "kubectl",
            "delete",
            "pod",
            "-l",
            "app=sample-app"
        ])
 
    @staticmethod
    def run_cpu_hog():
 
        print(
            "Invoking Harness CPU Hog Experiment"
        )
 
    @staticmethod
    def run_network_loss():
 
        print(
            "Invoking Harness Network Loss Experiment"
        )