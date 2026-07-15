class InsightEngine:

    def generate(self, workbook):

        insights = []

        business_health = workbook.get(
            "business_health",
            {}
        )

        quality = workbook.get(
            "data_quality",
            {}
        )

        domain = workbook.get(
            "domain",
            {}
        ).get(
            "name",
            "General"
        )

        for sheet in workbook.get("worksheets", []):

            sheet_insights = []

            meanings = sheet.get(
                "business_meaning",
                {}
            )

            statistics = sheet.get(
                "statistics",
                {}
            )

            # --------------------------------------------------
            # Executive Dataset Insight
            # --------------------------------------------------

            sheet_insights.append({

                "category": "Executive",

                "severity": "success",

                "icon": "🏢",

                "title": "Business Domain",

                "message":
                f"This worksheet belongs to the {domain} business domain."

            })

            # --------------------------------------------------
            # Business Metrics
            # --------------------------------------------------

            for column, info in meanings.items():

                if info.get(
                    "business_category"
                ) != "Measure":

                    continue

                metric = info.get(
                    "business_name",
                    column
                )

                stats = statistics.get(
                    column,
                    {}
                )

                total = stats.get(
                    "sum",
                    0
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

                median = stats.get(
                    "median",
                    0
                )

                count = stats.get(
                    "count",
                    0
                )

                if total > 0:

                    sheet_insights.append({

                        "category": "Business",

                        "severity": "success",

                        "icon": "💰",

                        "title": f"{metric} Summary",

                        "message":
                        f"Total {metric.lower()} recorded is {total:,.2f}."

                    })

                if average > 0:

                    sheet_insights.append({

                        "category": "Performance",

                        "severity": "info",

                        "icon": "📊",

                        "title": f"Average {metric}",

                        "message":
                        f"Average {metric.lower()} is {average:,.2f}."

                    })

                if maximum > average * 2 and average > 0:

                    sheet_insights.append({

                        "category": "Risk",

                        "severity": "warning",

                        "icon": "⚠️",

                        "title": "Exceptional High Value",

                        "message":
                        f"Some {metric.lower()} values are unusually high and should be verified."

                    })

                if minimum < average * 0.25 and average > 0:

                    sheet_insights.append({

                        "category": "Opportunity",

                        "severity": "info",

                        "icon": "💡",

                        "title": "Improvement Opportunity",

                        "message":
                        f"Very low {metric.lower()} values were identified. Investigate the underlying business process."

                    })

                if median != average:

                    sheet_insights.append({

                        "category": "Analytics",

                        "severity": "info",

                        "icon": "📈",

                        "title": "Distribution Variation",

                        "message":
                        f"The distribution of {metric.lower()} indicates possible skewness or outliers."

                    })

                if count > 0:

                    sheet_insights.append({

                        "category": "Analytics",

                        "severity": "success",

                        "icon": "📋",

                        "title": "Observation",

                        "message":
                        f"{count:,} business records were analysed for {metric.lower()}."

                    })

            # --------------------------------------------------
            # Data Quality
            # --------------------------------------------------

            if quality.get("missing", 0) > 0:

                sheet_insights.append({

                    "category": "Quality",

                    "severity": "warning",

                    "icon": "🟡",

                    "title": "Missing Values",

                    "message":
                    f"{quality.get('missing')} missing values detected."

                })

            if quality.get("duplicates", 0) > 0:

                sheet_insights.append({

                    "category": "Quality",

                    "severity": "warning",

                    "icon": "🔄",

                    "title": "Duplicate Records",

                    "message":
                    f"{quality.get('duplicates')} duplicate records detected."

                })

            # --------------------------------------------------
            # Business Health
            # --------------------------------------------------

            sheet_insights.append({

                "category": "Executive",

                "severity": "success",

                "icon": "🧠",

                "title": "Business Health",

                "message":
                f"Overall business health score is {business_health.get('health_score',0)}%."

            })

            sheet_insights.append({

                "category": "Executive",

                "severity": "success",

                "icon": "🤖",

                "title": "AI Confidence",

                "message":
                f"AI confidence score is {business_health.get('confidence_score',0)}%."

            })

            sheet_insights.append({

                "sheet": sheet["sheet_name"],

                "items": sheet_insights

            })

        workbook["insights"] = insights

        return workbook