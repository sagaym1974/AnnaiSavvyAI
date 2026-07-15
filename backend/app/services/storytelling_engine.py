class StorytellingEngine:

    def generate(self, workbook):

        stories = []

        domain = workbook.get(
            "domain",
            {}
        ).get(
            "name",
            "General"
        )

        health = workbook.get(
            "business_health",
            {}
        )

        quality = workbook.get(
            "data_quality",
            {}
        )

        executive = workbook.get(
            "executive_intelligence",
            {}
        )

        stories.append(

            f"The uploaded workbook belongs to the {domain} domain."

        )

        stories.append(

            f"Business Health Score is {health.get('health_score',0)}%."

        )

        stories.append(

            f"Data Quality Score is {quality.get('score',0)}%."

        )

        forecast = executive.get(
            "forecast_readiness",
            {}
        )

        stories.append(

            f"The workbook is {forecast.get('status','Unknown')} for forecasting."

        )

        recommendations = executive.get(
            "top_recommendations",
            []
        )

        if recommendations:

            stories.append(

                f"The highest priority recommendation is '{recommendations[0].get('title','')}'."

            )

        workbook["storytelling"] = {

            "story": " ".join(stories),

            "paragraphs": stories

        }

        return workbook