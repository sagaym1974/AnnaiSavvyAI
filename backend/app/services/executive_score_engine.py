class ExecutiveScoreEngine:

    def generate(self, workbook):

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

        health_score = health.get(
            "health_score",
            0
        )

        quality_score = quality.get(
            "score",
            0
        )

        confidence_score = executive.get(
            "confidence",
            {}
        ).get(
            "score",
            0
        )

        forecast_score = executive.get(
            "forecast_readiness",
            {}
        ).get(
            "score",
            0
        )

        executive_score = round(

            (

                health_score * 0.35 +

                quality_score * 0.30 +

                confidence_score * 0.20 +

                forecast_score * 0.15

            ),

            2

        )

        if executive_score >= 90:

            status = "Excellent"

            color = "#2E7D32"

        elif executive_score >= 80:

            status = "Very Good"

            color = "#1976D2"

        elif executive_score >= 70:

            status = "Good"

            color = "#F9A825"

        elif executive_score >= 60:

            status = "Average"

            color = "#EF6C00"

        else:

            status = "Critical"

            color = "#C62828"

        executive["executive_score"] = executive_score

        executive["dashboard_status"] = {

            "status": status,

            "color": color

        }

        workbook["executive_intelligence"] = executive

        return workbook