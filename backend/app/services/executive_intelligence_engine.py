class ExecutiveIntelligenceEngine:

    def generate(self, workbook):

        business_health = workbook.get(
            "business_health",
            {}
        )

        data_quality = workbook.get(
            "data_quality",
            {}
        )

        domain = workbook.get(
            "domain",
            {}
        )

        recommendations = workbook.get(
            "recommendations",
            []
        )

        charts = workbook.get(
            "charts",
            []
        )

        kpis = workbook.get(
            "kpis",
            []
        )

        executive = {

            "domain": domain,

            "business_health": business_health,

            "data_quality": data_quality,

            "summary": "",

            "risks": [],

            "opportunities": [],

            "top_kpis": [],

            "top_charts": [],

            "top_insights": [],

            "top_recommendations": [],

            "forecast_readiness": {},

            "confidence": {},

            "dashboard_status": {},

            "executive_score": 0

        }

        # ---------------------------------------------------
        # KPI Selection
        # ---------------------------------------------------

        executive["top_kpis"] = sorted(

            kpis,

            key=lambda x: (

                x.get("priority", 99),

                str(x.get("title"))

            )

        )[:8]

        # ---------------------------------------------------
        # Chart Selection
        # ---------------------------------------------------

        executive["top_charts"] = sorted(

            charts,

            key=lambda x: (

                x.get("priority", 99),

                x.get("chart_type", "")

            )

        )[:6]

        # ---------------------------------------------------
        # Insight Selection
        # ---------------------------------------------------

        all_insights = []

        for sheet in workbook.get(

            "insights",

            []

        ):

            all_insights.extend(

                sheet.get(

                    "items",

                    []

                )

            )

        executive["top_insights"] = all_insights[:10]

        # ---------------------------------------------------
        # Recommendations
        # ---------------------------------------------------

        executive["top_recommendations"] = recommendations[:8]

        # ---------------------------------------------------
        # Risks & Opportunities
        # ---------------------------------------------------

        for item in all_insights:

            category = item.get(

                "category",

                ""

            )

            if category == "Risk":

                executive["risks"].append(item)

            elif category == "Opportunity":

                executive["opportunities"].append(item)

        # ---------------------------------------------------
        # Forecast Readiness
        # ---------------------------------------------------

        quality_score = data_quality.get(

            "score",

            100

        )

        if quality_score >= 95:

            readiness = "Excellent"

        elif quality_score >= 85:

            readiness = "Very Good"

        elif quality_score >= 70:

            readiness = "Good"

        elif quality_score >= 50:

            readiness = "Average"

        else:

            readiness = "Poor"

        executive["forecast_readiness"] = {

            "score": quality_score,

            "status": readiness

        }

        # ---------------------------------------------------
        # AI Confidence
        # ---------------------------------------------------

        confidence_score = business_health.get(

            "confidence_score",

            0

        )

        executive["confidence"] = {

            "score": confidence_score,

            "status":

                "Excellent"

                if confidence_score >= 90 else

                "Good"

                if confidence_score >= 75 else

                "Average"

                if confidence_score >= 60 else

                "Low"

        }

        # ---------------------------------------------------
        # Executive Score
        # ---------------------------------------------------

        executive_score = int(

            (

                business_health.get(

                    "health_score",

                    0

                )

                +

                quality_score

                +

                confidence_score

            ) / 3

        )

        executive["executive_score"] = executive_score

        # ---------------------------------------------------
        # Dashboard Status
        # ---------------------------------------------------

        executive["dashboard_status"] = {

            "status":

                "Healthy"

                if executive_score >= 90 else

                "Good"

                if executive_score >= 75 else

                "Needs Attention"

                if executive_score >= 60 else

                "Critical"

        }

        # ---------------------------------------------------
        # Executive Summary
        # ---------------------------------------------------

        executive["summary"] = (

            f"The uploaded workbook has been analysed successfully. "

            f"The detected business domain is "

            f"{domain.get('name','General')}. "

            f"The overall Business Health Score is "

            f"{business_health.get('health_score',0)}%. "

            f"The Data Quality Score is "

            f"{quality_score}%. "

            f"AI Confidence is "

            f"{confidence_score}%. "

            f"The workbook is assessed as "

            f"{readiness} for forecasting and advanced analytics. "

            f"The overall Executive Score is "

            f"{executive_score}%. "

            f"{len(recommendations)} executive recommendations and "

            f"{len(all_insights)} business insights have been generated automatically."

        )

        workbook["executive_intelligence"] = executive

        return workbook