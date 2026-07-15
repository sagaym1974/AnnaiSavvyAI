
class ChartEngine:
    """Enterprise Chart Engine."""

    def generate(self, workbook):

        charts = []

        domain = workbook.get("domain", {}).get("name", "General")

        for sheet in workbook.get("worksheets", []):

            meanings = sheet.get("business_meaning", {})

            raw_data = sheet.get("sample_data", [])
            formatted_data = sheet.get("presentation_data", [])

            if not raw_data:
                continue

            data = []

            for i, row in enumerate(raw_data):
                new_row = row.copy()

                if i < len(formatted_data):
                    for column, info in meanings.items():
                        if info.get("semantic") == "Date":
                            new_row[column] = formatted_data[i].get(column, row.get(column))

                data.append(new_row)

            dimensions = []
            measures = []
            dates = []

            for column, info in meanings.items():
                if info.get("business_category") == "Measure":
                    measures.append(column)
                else:
                    dimensions.append(column)

                if info.get("semantic") == "Date":
                    dates.append(column)

            if dimensions and measures:
                charts.append({
                    "sheet": sheet["sheet_name"],
                    "priority": 1,
                    "chart_type": "bar",
                    "title": f"{meanings[measures[0]]['display_name']} by {self.display_name(dimensions[0])}",
                    "x_axis": dimensions[0],
                    "y_axis": measures[0],
                    "business_metric": meanings[measures[0]]["business_name"],
                    "domain": domain,
                    "data": data
                })

            if dates and measures:
                charts.append({
                    "sheet": sheet["sheet_name"],
                    "priority": 2,
                    "chart_type": "line",
                    "title": f"{meanings[measures[0]]['display_name']} Trend",
                    "x_axis": dates[0],
                    "y_axis": measures[0],
                    "business_metric": meanings[measures[0]]["business_name"],
                    "domain": domain,
                    "data": data
                })

            if dimensions and measures:
                charts.append({
                    "sheet": sheet["sheet_name"],
                    "priority": 3,
                    "chart_type": "pie",
                    "title": f"{meanings[measures[0]]['display_name']} Distribution",
                    "label": dimensions[0],
                    "value": measures[0],
                    "business_metric": meanings[measures[0]]["business_name"],
                    "domain": domain,
                    "data": data
                })

            if len(measures) >= 2:
                scatter = []
                for row in raw_data:
                    try:
                        scatter.append({
                            measures[0]: float(row[measures[0]]),
                            measures[1]: float(row[measures[1]])
                        })
                    except Exception:
                        pass

                if scatter:
                    charts.append({
                        "sheet": sheet["sheet_name"],
                        "priority": 4,
                        "chart_type": "scatter",
                        "title": f"{meanings[measures[0]]['display_name']} vs {meanings[measures[1]]['display_name']}",
                        "x_axis": measures[0],
                        "y_axis": measures[1],
                        "business_metric": meanings[measures[0]]["business_name"],
                        "domain": domain,
                        "data": scatter
                    })

            if dates and measures:
                charts.append({
                    "sheet": sheet["sheet_name"],
                    "priority": 5,
                    "chart_type": "area",
                    "title": f"{meanings[measures[0]]['display_name']} Growth",
                    "x_axis": dates[0],
                    "y_axis": measures[0],
                    "business_metric": meanings[measures[0]]["business_name"],
                    "domain": domain,
                    "data": data
                })

            if dimensions and measures:
                charts.append({
                    "sheet": sheet["sheet_name"],
                    "priority": 6,
                    "chart_type": "horizontal_bar",
                    "title": f"Top {self.display_name(dimensions[0])}",
                    "x_axis": measures[0],
                    "y_axis": dimensions[0],
                    "business_metric": meanings[measures[0]]["business_name"],
                    "domain": domain,
                    "data": data
                })

        workbook["charts"] = sorted(
            charts,
            key=lambda x: (x["priority"], x["chart_type"])
        )

        return workbook

    def display_name(self, column):
        return " ".join(str(column).replace("_", " ").split()).title()
