from assessment.assessment_runner import AssessmentRunner
 
 
def main():
 
    target_url = (
        "http://localhost:5000/api/orders"
    )
 
    runner = AssessmentRunner()
 
    result = runner.run(
        target_url
    )
 
    print("\nAssessment Complete\n")
    print(result)
 
 
if __name__ == "__main__":
    main()