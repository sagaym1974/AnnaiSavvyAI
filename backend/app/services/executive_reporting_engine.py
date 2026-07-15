class ExecutiveReportingEngine:

    def generate(self, workbook):

        report = {}

        report["cover"] = {

            "title": "Executive Business Intelligence Report",

            "file":

                workbook.get(
                    "filename",
                    ""
                )

        }

        report["summary"] = workbook.get(
            "ai_summary",
            {}
        )

        report["dashboard"] = workbook.get(
            "dashboard",
            {}
        )

        report["narrative"] = workbook.get(
            "narrative",
            {}
        )

        report["storytelling"] = workbook.get(
            "storytelling",
            {}
        )

        report["alerts"] = workbook.get(
            "executive_alerts",
            []
        )

        report["recommendations"] = workbook.get(
            "recommendations",
            []
        )

        report["risks"] = workbook.get(
            "risks",
            []
        )

        report["opportunities"] = workbook.get(
            "opportunities",
            []
        )

        workbook["executive_report"] = report

        return workbook