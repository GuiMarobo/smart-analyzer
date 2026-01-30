from infrastructure.repository.ticket_repository_csv import TicketRepositoryCSV
from services.classification.ml_classifier import MLClassifier
from services.insights.default_insights import DefaultInsightGenerator
from application.analyze_tickets_use_case import AnalyzeTicketsUseCase

def main():
    use_case = AnalyzeTicketsUseCase(
        repository=TicketRepositoryCSV(),
        classifier=MLClassifier(),
        insight_generator=DefaultInsightGenerator()
    )

    insights, df = use_case.execute()

    print("SMART TICKET\n")

    print("INSIGHTS:")
    for insight in insights:
        print("-", insight)

    print("\nPREDICTED CATEGORIES:")
    print(df[["description", "category", "predicted_category"]])

if __name__ == "__main__":
    main()
