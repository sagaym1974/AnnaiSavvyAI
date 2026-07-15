class AISummaryEngine:

    def generate(self, workbook):

        executive = workbook.get(
            "executive_intelligence",
            {}
        )

        scorecard = workbook.get(
            "scorecard",
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

        summary = {

            "title": "AI Executive Summary",

            "business_domain":

                workbook.get(
                    "domain",
                    {}
                ).get(
                    "name",
                    "General"
                ),

            "executive_score":

                scorecard.get(
                    "executive_score",
                    0
                ),

            "health_score":

                health.get(
                    "health_score",
                    0
                ),

            "quality_score":

                quality.get(
                    "score",
                    0
                ),

            "forecast":

                executive.get(
                    "forecast_readiness",
                    {}
                ).get(
                    "status",
                    "Unknown"
                ),

            "summary":

                executive.get(
                    "summary",
                    ""
                )

        }

        workbook["ai_summary"] = summary

        return workbook