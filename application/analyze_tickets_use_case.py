class AnalyzeTicketsUseCase:

    def __init__(self, repository, classifier, insight_generator):
        self.repository = repository
        self.classifier = classifier
        self.insight_generator = insight_generator

    def execute(self):
        df = self.repository.load()

        if hasattr(self.classifier, "train"):
            self.classifier.train(
                df["description"],
                df["category"]
            )

        df["predicted_category"] = df["description"].apply(
            self.classifier.classify
        )

        insights = self.insight_generator.generate(df)
        return insights, df
