import pandas as pd


class KPIEngine:

    def generate(self, workbook):

        kpis = []

        for sheet in workbook["worksheets"]:

            sheet_name = sheet["sheet_name"]

            sample = sheet["sample_data"]

            df = pd.DataFrame(sample)

            kpis.extend(

                self.basic_kpis(sheet)

            )

            kpis.extend(

                self.sales_kpis(sheet_name, df)

            )

            kpis.extend(

                self.hr_kpis(sheet_name, df)

            )

        workbook["kpis"] = kpis

        return workbook

    def basic_kpis(self, sheet):

        return [

            {

                "sheet": sheet["sheet_name"],

                "name": "Total Rows",

                "value": sheet["rows"]

            },

            {

                "sheet": sheet["sheet_name"],

                "name": "Total Columns",

                "value": sheet["columns"]

            },

            {

                "sheet": sheet["sheet_name"],

                "name": "Dataset Type",

                "value": sheet["dataset_type"]

            }

        ]

    def sales_kpis(self, sheet_name, df):

        if "Amount" not in df.columns:

            return []

        result = [

            {

                "sheet": sheet_name,

                "name": "Total Sales",

                "value": float(df["Amount"].sum())

            },

            {

                "sheet": sheet_name,

                "name": "Average Sale",

                "value": float(df["Amount"].mean())

            },

            {

                "sheet": sheet_name,

                "name": "Highest Sale",

                "value": float(df["Amount"].max())

            },

            {

                "sheet": sheet_name,

                "name": "Lowest Sale",

                "value": float(df["Amount"].min())

            }

        ]

        if "Qty" in df.columns:

            result.append(

                {

                    "sheet": sheet_name,

                    "name": "Total Quantity",

                    "value": int(df["Qty"].sum())

                }

            )

        return result

    def hr_kpis(self, sheet_name, df):

        if "Department" not in df.columns:

            return []

        return [

            {

                "sheet": sheet_name,

                "name": "Employee Count",

                "value": len(df)

            },

            {

                "sheet": sheet_name,

                "name": "Departments",

                "value": df["Department"].nunique()

            }

        ]