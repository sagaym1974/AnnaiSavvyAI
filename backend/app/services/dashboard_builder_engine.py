class DashboardBuilderEngine:

    def generate(self, workbook):

        dashboard = {}

        dashboard["executive"] = workbook.get(
            "executive_intelligence",
            {}
        )

        dashboard["scorecard"] = workbook.get(
            "scorecard",
            {}
        )

        dashboard["alerts"] = workbook.get(
            "executive_alerts",
            []
        )

        dashboard["recommendations"] = workbook.get(
            "recommendations",
            []
        )[:10]

        dashboard["risks"] = workbook.get(
            "risks",
            []
        )[:10]

        dashboard["opportunities"] = workbook.get(
            "opportunities",
            []
        )[:10]

        dashboard["kpis"] = workbook.get(
            "kpis",
            []
        )[:12]

        dashboard["charts"] = workbook.get(
            "charts",
            []
        )[:8]

        dashboard["forecast"] = workbook.get(
            "forecast_ai",
            {}
        )

        dashboard["story"] = workbook.get(
            "storytelling",
            {}
        )

        workbook["dashboard"] = dashboard

        return workbook