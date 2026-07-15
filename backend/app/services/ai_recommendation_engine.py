class AIRecommendationEngine:

    def generate(self, executive):

        recommendations = []

        health = executive.get(
            "business_health",
            {}
        )

        quality = executive.get(
            "data_quality",
            {}
        )

        confidence = executive.get(
            "confidence",
            {}
        )

        forecast = executive.get(
            "forecast_readiness",
            {}
        )

        executive_score = executive.get(
            "executive_score",
            0
        )

        # --------------------------------------------------
        # Executive Score
        # --------------------------------------------------

        if executive_score < 60:

            recommendations.append({

                "priority": "Critical",

                "category": "Executive",

                "title": "Executive Intervention Required",

                "message":
                "Overall executive score is critically low. Immediate management attention is recommended."

            })

        elif executive_score < 80:

            recommendations.append({

                "priority": "High",

                "category": "Executive",

                "title": "Improve Overall Business Performance",

                "message":
                "Business performance is acceptable but several improvement opportunities exist."

            })

        # --------------------------------------------------
        # Business Health
        # --------------------------------------------------

        if health.get("health_score", 100) < 70:

            recommendations.append({

                "priority": "High",

                "category": "Business",

                "title": "Improve Business Health",

                "message":
                "Review operational KPIs, remove bottlenecks and improve overall business efficiency."

            })

        if health.get("risk_level") in [

            "High",

            "Critical"

        ]:

            recommendations.append({

                "priority": "High",

                "category": "Risk",

                "title": "Reduce Business Risks",

                "message":
                "Several business risks were detected. Investigate anomalies and operational issues."

            })

        # --------------------------------------------------
        # Data Quality
        # --------------------------------------------------

        if quality.get("score", 100) < 90:

            recommendations.append({

                "priority": "High",

                "category": "Data",

                "title": "Improve Data Quality",

                "message":
                "Remove duplicates, fill missing values and improve workbook quality before executive reporting."

            })

        if quality.get("duplicates", 0) > 0:

            recommendations.append({

                "priority": "Medium",

                "category": "Data",

                "title": "Remove Duplicate Records",

                "message":
                f"{quality.get('duplicates')} duplicate records were detected."

            })

        if quality.get("missing", 0) > 0:

            recommendations.append({

                "priority": "Medium",

                "category": "Data",

                "title": "Complete Missing Information",

                "message":
                f"{quality.get('missing')} missing values should be completed."

            })

        # --------------------------------------------------
        # AI Confidence
        # --------------------------------------------------

        if confidence.get("score", 100) < 75:

            recommendations.append({

                "priority": "Medium",

                "category": "AI",

                "title": "Increase AI Confidence",

                "message":
                "Upload larger datasets with historical records to improve AI intelligence."

            })

        # --------------------------------------------------
        # Forecast
        # --------------------------------------------------

        if forecast.get("status") not in [

            "Excellent",

            "Very Good"

        ]:

            recommendations.append({

                "priority": "Medium",

                "category": "Forecast",

                "title": "Improve Forecast Readiness",

                "message":
                "Additional historical business data will improve forecasting accuracy."

            })

        # --------------------------------------------------
        # Executive Success
        # --------------------------------------------------

        if not recommendations:

            recommendations.append({

                "priority": "Low",

                "category": "Executive",

                "title": "Excellent Business Performance",

                "message":
                "Business health, data quality and AI confidence are excellent. Continue monitoring KPIs and business trends."

            })

        priority_order = {

            "Critical": 1,

            "High": 2,

            "Medium": 3,

            "Low": 4

        }

        recommendations = sorted(

            recommendations,

            key=lambda x: (

                priority_order.get(

                    x["priority"],

                    99

                ),

                x["title"]

            )

        )

        return recommendations