from services.insights.insight_generator import InsightGenerator

class DefaultInsightGenerator(InsightGenerator):

    def generate(self, df):
        insights = []
        insights.append(self._most_common_category(df))
        insights.append(self._highest_avg_resolution(df))
        insights.append(self._high_priority_count(df))
        return insights

    def _most_common_category(self, df):
        category = df["category"].value_counts().idxmax()
        return f"Most tickets belong to the '{category}' category."

    def _highest_avg_resolution(self, df):
        category = (
            df.groupby("category")["resolution_time_hours"]
            .mean()
            .idxmax()
        )
        return f"'{category}' has the highest average resolution time."

    def _high_priority_count(self, df):
        count = df[df["priority"] == "High"].shape[0]
        return f"There are {count} high-priority tickets requiring attention."
