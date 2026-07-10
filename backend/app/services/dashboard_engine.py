class DashboardEngine:

    def generate(self, workbook):

        dashboard = {

            "title": "Annai Savvy AI Dashboard",

            "cards": [],

            "charts": []

        }

        for kpi in workbook["kpis"]:

            dashboard["cards"].append(

                {

                    "title": kpi["name"],

                    "value": kpi["value"],

                    "sheet": kpi["sheet"]

                }

            )

        for chart in workbook["charts"]:

            dashboard["charts"].append(chart)

        workbook["dashboard"] = dashboard

        return workbook