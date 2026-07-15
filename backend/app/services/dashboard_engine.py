class DashboardEngine:

    def generate(self, workbook):

        dashboard = {}

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

        context = workbook.get(
            "workbook_context",
            {}
        )

        # --------------------------------------------------
        # Executive Overview
        # --------------------------------------------------

        dashboard["overview"] = {

            "business_domain":

                executive.get(
                    "domain",
                    {}
                ).get(
                    "name",
                    "General"
                ),

            "executive_score":

                executive.get(
                    "executive_score",
                    0
                ),

            "dashboard_status":

                executive.get(
                    "dashboard_status",
                    {}
                ).get(
                    "status",
                    "Unknown"
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

            "confidence":

                executive.get(
                    "confidence",
                    {}
                ).get(
                    "score",
                    0
                )

        }

        # --------------------------------------------------
        # Workbook Summary
        # --------------------------------------------------

        dashboard["workbook"] = {

            "worksheets":

                context.get(
                    "worksheet_count",
                    0
                ),

            "rows":

                context.get(
                    "row_count",
                    0
                ),

            "columns":

                context.get(
                    "column_count",
                    0
                ),

            "largest_sheet":

                context.get(
                    "largest_sheet",
                    ""
                ),

            "dominant_dataset":

                context.get(
                    "dominant_dataset",
                    ""
                )

        }

        # --------------------------------------------------
        # KPI Dashboard
        # --------------------------------------------------

        dashboard["top_kpis"] = sorted(

            workbook.get(

                "kpis",

                []

            ),

            key=lambda x: (

                x.get(

                    "priority",

                    999

                ),

                str(

                    x.get(

                        "title",

                        ""

                    )

                )

            )

        )[:12]

        # --------------------------------------------------
        # Charts
        # --------------------------------------------------

        dashboard["top_charts"] = sorted(

            workbook.get(

                "charts",

                []

            ),

            key=lambda x: (

                x.get(

                    "priority",

                    999

                ),

                x.get(

                    "chart_type",

                    ""

                )

            )

        )[:8]

        # --------------------------------------------------
        # Insights
        # --------------------------------------------------

        insights = []

        for sheet in workbook.get(

            "insights",

            []

        ):

            insights.extend(

                sheet.get(

                    "items",

                    []

                )

            )

        dashboard["top_insights"] = insights[:15]

        # --------------------------------------------------
        # Recommendations
        # --------------------------------------------------

        dashboard["top_recommendations"] = workbook.get(

            "recommendations",

            []

        )[:10]

        # --------------------------------------------------
        # Risks
        # --------------------------------------------------

        dashboard["risks"] = executive.get(

            "risks",

            []

        )[:10]

        # --------------------------------------------------
        # Opportunities
        # --------------------------------------------------

        dashboard["opportunities"] = executive.get(

            "opportunities",

            []

        )[:10]

        # --------------------------------------------------
        # Forecast
        # --------------------------------------------------

        dashboard["forecast"] = executive.get(

            "forecast_readiness",

            {}

        )

        # --------------------------------------------------
        # Executive Summary
        # --------------------------------------------------

        dashboard["executive_summary"] = executive.get(

            "summary",

            ""

        )

        # --------------------------------------------------
        # Dashboard Metadata
        # --------------------------------------------------

        dashboard["statistics"] = {

            "total_kpis":

                len(

                    workbook.get(

                        "kpis",

                        []

                    )

                ),

            "total_charts":

                len(

                    workbook.get(

                        "charts",

                        []

                    )

                ),

            "total_insights":

                len(

                    insights

                ),

            "total_recommendations":

                len(

                    workbook.get(

                        "recommendations",

                        []

                    )

                )

        }

        workbook["dashboard"] = dashboard

        workbook["executive_dashboard"] = dashboard

        return workbook