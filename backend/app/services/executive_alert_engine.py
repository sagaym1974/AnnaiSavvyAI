class ExecutiveAlertEngine:

    def generate(self, workbook):

        alerts = []

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

        forecast = executive.get(
            "forecast_readiness",
            {}
        )

        if health.get("health_score", 100) < 70:

            alerts.append({

                "type": "Business",

                "priority": "High",

                "title": "Business Health Warning",

                "message":
                "Business health is below the recommended threshold."

            })

        if quality.get("score", 100) < 85:

            alerts.append({

                "type": "Data Quality",

                "priority": "High",

                "title": "Poor Data Quality",

                "message":
                "Missing values or duplicates are affecting analytics."

            })

        if confidence.get("score", 100) < 75:

            alerts.append({

                "type": "AI",

                "priority": "Medium",

                "title": "Low AI Confidence",

                "message":
                "Upload additional historical data for better predictions."

            })

        if forecast.get("status") == "Poor":

            alerts.append({

                "type": "Forecast",

                "priority": "Medium",

                "title": "Forecast Not Reliable",

                "message":
                "Current workbook is not suitable for forecasting."

            })

        if len(alerts) == 0:

            alerts.append({

                "type": "Healthy",

                "priority": "Low",

                "title": "Workbook Healthy",

                "message":
                "No significant executive alerts detected."

            })

        workbook["executive_alerts"] = alerts

        return workbook