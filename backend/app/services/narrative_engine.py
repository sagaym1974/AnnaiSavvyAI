class NarrativeEngine:

    def generate(self, workbook):

        executive = workbook.get(
            "executive_intelligence",
            {}
        )

        health = workbook.get(
            "business_health",
            {}
        )

        quality = workbook.get(
            "data_quality",
            {}
        )

        score = executive.get(
            "executive_score",
            0
        )

        paragraphs = []

        paragraphs.append(

            f"This workbook belongs to the {workbook.get('domain',{}).get('name','General')} business domain."

        )

        paragraphs.append(

            f"The Business Health Score is {health.get('health_score',0)}%."

        )

        paragraphs.append(

            f"The Data Quality Score is {quality.get('score',0)}%."

        )

        paragraphs.append(

            f"The Executive Score is {score}%."

        )

        if score >= 90:

            paragraphs.append(

                "Overall business performance is excellent."

            )

        elif score >= 75:

            paragraphs.append(

                "Business performance is healthy with opportunities for optimization."

            )

        elif score >= 60:

            paragraphs.append(

                "Business performance requires management attention."

            )

        else:

            paragraphs.append(

                "Critical business intervention is recommended."

            )

        workbook["narrative"] = {

            "paragraphs": paragraphs,

            "text": " ".join(paragraphs)

        }

        return workbook