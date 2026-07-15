class RecommendationEngine:

    def generate(self, workbook):

        recommendations = []

        quality = workbook.get(
            "data_quality",
            {}
        )

        health = workbook.get(
            "business_health",
            {}
        )

        domain = workbook.get(
            "domain",
            {}
        )

        # -----------------------------------------
        # Executive Recommendations
        # -----------------------------------------

        if health.get("health_score", 100) < 60:

            recommendations.append({

                "priority": 1,

                "category": "Executive",

                "title": "Immediate Management Review",

                "message":
                "Overall business health is critically low. Executive intervention is recommended immediately."

            })

        elif health.get("health_score", 100) < 80:

            recommendations.append({

                "priority": 2,

                "category": "Executive",

                "title": "Improve Business Performance",

                "message":
                "Business health is moderate. Review operational KPIs and improve overall performance."

            })

        # -----------------------------------------
        # Data Quality
        # -----------------------------------------

        if quality.get("missing", 0) > 0:

            recommendations.append({

                "priority": 3,

                "category": "Data Quality",

                "title": "Complete Missing Information",

                "message":
                f"{quality.get('missing')} missing values detected. Complete the missing information before publishing reports."

            })

        if quality.get("duplicates", 0) > 0:

            recommendations.append({

                "priority": 4,

                "category": "Data Quality",

                "title": "Remove Duplicate Records",

                "message":
                f"{quality.get('duplicates')} duplicate records detected. Removing duplicates will improve reporting accuracy."

            })

        if quality.get("empty_columns", 0) > 0:

            recommendations.append({

                "priority": 5,

                "category": "Data Quality",

                "title": "Remove Empty Columns",

                "message":
                "Unused columns were detected. Removing them will improve workbook quality."

            })

        # -----------------------------------------
        # Business Metrics
        # -----------------------------------------

        for sheet in workbook.get(
            "worksheets",
            []
        ):

            meanings = sheet.get(
                "business_meaning",
                {}
            )

            for column, info in meanings.items():

                if info.get(
                    "business_category"
                ) != "Measure":

                    continue

                metric = info.get(
                    "business_name",
                    column
                )

                stats = info.get(
                    "statistics",
                    {}
                )

                average = stats.get(
                    "average",
                    0
                )

                maximum = stats.get(
                    "maximum",
                    0
                )

                minimum = stats.get(
                    "minimum",
                    0
                )

                total = stats.get(
                    "sum",
                    0
                )

                if average == 0:

                    continue

                if maximum >= average * 2:

                    recommendations.append({

                        "priority": 10,

                        "category": "Business",

                        "title": f"Review High {metric}",

                        "message":
                        f"The highest {metric.lower()} is significantly above the average. Verify exceptional transactions."

                    })

                if minimum <= average * 0.25:

                    recommendations.append({

                        "priority": 11,

                        "category": "Business",

                        "title": f"Improve Low {metric}",

                        "message":
                        f"Very low {metric.lower()} values were detected. Investigate underperforming business areas."

                    })

                if total > average * 100:

                    recommendations.append({

                        "priority": 12,

                        "category": "Growth",

                        "title": f"Strong {metric} Potential",

                        "message":
                        f"The workbook indicates strong overall {metric.lower()} performance. Consider expanding successful business operations."

                    })

        # -----------------------------------------
        # Domain Specific
        # -----------------------------------------

        domain_name = domain.get(
            "name",
            "General"
        )

        if domain_name == "Sales":

            recommendations.append({

                "priority": 20,

                "category": "Sales",

                "title": "Strengthen Customer Analytics",

                "message":
                "Monitor customer buying behaviour, product mix and regional performance regularly."

            })

        elif domain_name == "Finance":

            recommendations.append({

                "priority": 20,

                "category": "Finance",

                "title": "Improve Financial Planning",

                "message":
                "Monitor cash flow, expenses and profitability using monthly trend analysis."

            })

        elif domain_name == "HR":

            recommendations.append({

                "priority": 20,

                "category": "HR",

                "title": "Monitor Workforce Performance",

                "message":
                "Review employee productivity, attendance and payroll trends regularly."

            })

        elif domain_name == "Inventory":

            recommendations.append({

                "priority": 20,

                "category": "Inventory",

                "title": "Optimize Inventory Levels",

                "message":
                "Monitor slow-moving inventory and replenish fast-moving products proactively."

            })

        # -----------------------------------------
        # Healthy Business
        # -----------------------------------------

        if len(recommendations) == 0:

            recommendations.append({

                "priority": 99,

                "category": "Executive",

                "title": "Excellent Business Health",

                "message":
                "No significant risks were detected. Continue monitoring KPIs and maintain current business practices."

            })

        recommendations = sorted(

            recommendations,

            key=lambda x: x["priority"]

        )

        workbook["recommendations"] = recommendations

        return workbook