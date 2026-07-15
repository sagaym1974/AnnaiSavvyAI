class BusinessHealthEngine:

    def generate(self, workbook):

        quality = workbook.get(
            "data_quality",
            {}
        )

        anomalies = workbook.get(
            "anomalies",
            []
        )

        worksheets = workbook.get(
            "worksheets",
            []
        )

        # -----------------------------------------
        # Initial Scores
        # -----------------------------------------

        quality_score = quality.get(
            "score",
            100
        )

        risk_score = 0

        # -----------------------------------------
        # Data Quality Risks
        # -----------------------------------------

        risk_score += quality.get(
            "missing",
            0
        )

        risk_score += quality.get(
            "duplicates",
            0
        ) * 5

        risk_score += quality.get(
            "empty_columns",
            0
        ) * 5

        # -----------------------------------------
        # AI Anomaly Risks
        # -----------------------------------------

        risk_score += len(
            anomalies
        ) * 8

        # -----------------------------------------
        # Worksheet Complexity
        # -----------------------------------------

        if len(worksheets) <= 1:

            risk_score += 5

        elif len(worksheets) >= 10:

            risk_score += 10

        # -----------------------------------------
        # Numeric Analysis
        # -----------------------------------------

        numeric_columns = 0

        for sheet in worksheets:

            numeric_columns += len(

                sheet.get(

                    "numeric_columns",

                    []

                )

            )

        if numeric_columns == 0:

            risk_score += 25

        elif numeric_columns < 3:

            risk_score += 10

        # -----------------------------------------
        # Normalize
        # -----------------------------------------

        if risk_score > 100:

            risk_score = 100

        health_score = max(

            quality_score - int(risk_score * 0.45),

            0

        )

        opportunity_score = max(

            100 - risk_score,

            0

        )

        confidence_score = int(

            (

                health_score +

                quality_score +

                opportunity_score

            ) / 3

        )

        # -----------------------------------------
        # Business Status
        # -----------------------------------------

        if health_score >= 95:

            status = "Excellent"

            recommendation = (

                "The workbook is enterprise-grade and suitable "

                "for advanced AI analytics, forecasting and "

                "executive reporting."

            )

        elif health_score >= 85:

            status = "Very Good"

            recommendation = (

                "The workbook quality is very good. Minor "

                "improvements may further increase AI accuracy."

            )

        elif health_score >= 70:

            status = "Good"

            recommendation = (

                "Business data is reliable. Review highlighted "

                "issues before strategic decision making."

            )

        elif health_score >= 50:

            status = "Moderate"

            recommendation = (

                "Dataset requires cleansing before using "

                "predictive analytics."

            )

        else:

            status = "Critical"

            recommendation = (

                "Business dataset contains significant quality "

                "issues. Correct the data before executive "

                "reporting."

            )

        # -----------------------------------------
        # Risk Level
        # -----------------------------------------

        if risk_score < 20:

            risk_level = "Low"

        elif risk_score < 40:

            risk_level = "Moderate"

        elif risk_score < 70:

            risk_level = "High"

        else:

            risk_level = "Critical"

        # -----------------------------------------
        # AI Readiness
        # -----------------------------------------

        if confidence_score >= 90:

            ai_readiness = "Excellent"

        elif confidence_score >= 75:

            ai_readiness = "Good"

        elif confidence_score >= 60:

            ai_readiness = "Average"

        else:

            ai_readiness = "Poor"

        # -----------------------------------------
        # Store Result
        # -----------------------------------------

        workbook["business_health"] = {

            "health_score": health_score,

            "risk_score": risk_score,

            "risk_level": risk_level,

            "opportunity_score": opportunity_score,

            "confidence_score": confidence_score,

            "status": status,

            "ai_readiness": ai_readiness,

            "recommendation": recommendation

        }

        return workbook