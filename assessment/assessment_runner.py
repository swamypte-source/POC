from assessment.metrics_collector import MetricsCollector

from assessment.resilience_score import ResilienceScorer

from assessment.report_generator import ReportGenerator

 

 

class AssessmentRunner:

 

    def run(self, url):

 

        collector = MetricsCollector(url)

 

        metrics = collector.collect()

 

        result = ResilienceScorer.calculate(

            metrics

        )

 

        ReportGenerator.generate(result)

 

        return result