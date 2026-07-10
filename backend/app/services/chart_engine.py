class ChartEngine:

    def generate(self, workbook):

        charts = []

        for sheet in workbook["worksheets"]:

            columns = sheet["column_names"]

            chart_list = []

            # -------- Sales Trend --------

            if "Date" in columns and "Amount" in columns:

                chart_list.append(
                    {
                        "type": "line",
                        "title": "Sales Trend",
                        "x": "Date",
                        "y": "Amount"
                    }
                )

            # -------- Sales by Product --------

            if "Product" in columns and "Amount" in columns:

                chart_list.append(
                    {
                        "type": "bar",
                        "title": "Sales by Product",
                        "x": "Product",
                        "y": "Amount"
                    }
                )

            # -------- Quantity --------

            if "Product" in columns and "Qty" in columns:

                chart_list.append(
                    {
                        "type": "bar",
                        "title": "Quantity by Product",
                        "x": "Product",
                        "y": "Qty"
                    }
                )

            # -------- Department --------

            if "Department" in columns:

                chart_list.append(
                    {
                        "type": "pie",
                        "title": "Employees by Department",
                        "labels": "Department"
                    }
                )

            charts.extend(chart_list)

        workbook["charts"] = charts

        return workbook