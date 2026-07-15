class ScoringEngine:

    def generate(self, workbook):

        scorecard = {}

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

        confidence = executive.get(
            "confidence",
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

        confidence_score = confidence.get(
            "score",
            0
        )

        executive_score = round(

            (

                health_score * 0.40 +

                quality_score * 0.35 +

                confidence_score * 0.25

            ),

            2

        )

        if executive_score >= 90:

            grade = "A+"

            status = "Excellent"

        elif executive_score >= 80:

            grade = "A"

            status = "Very Good"

        elif executive_score >= 70:

            grade = "B"

            status = "Good"

        elif executive_score >= 60:

            grade = "C"

            status = "Average"

        elif executive_score >= 50:

            grade = "D"

            status = "Needs Improvement"

        else:

            grade = "F"

            status = "Critical"

        scorecard = {

            "executive_score":

                executive_score,

            "grade":

                grade,

            "status":

                status,

            "health_score":

                health_score,

            "quality_score":

                quality_score,

            "confidence_score":

                confidence_score

        }

        workbook["scorecard"] = scorecard

        return workbook