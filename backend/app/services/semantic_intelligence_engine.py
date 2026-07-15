class SemanticIntelligenceEngine:

    def generate(self, workbook):

        for sheet in workbook["worksheets"]:

            intelligence = {}

            sheet_name = sheet.get("sheet_name", "").lower()

            columns = sheet.get("column_names", [])

            semantics = sheet.get("semantics", {})

            for column in columns:

                name = column.lower()

                meaning = {}

                meaning["business_name"] = self.business_name(
                    sheet_name,
                    name,
                    semantics
                )

                meaning["business_category"] = self.business_category(
                    sheet_name,
                    name,
                    semantics
                )

                meaning["display_name"] = self.display_name(
                    meaning["business_name"]
                )

                intelligence[column] = meaning

            sheet["semantic_intelligence"] = intelligence

        return workbook

    def business_name(self, sheet_name, column_name, semantics):

        semantic = semantics.get(column_name, "Unknown")

        if semantic == "Currency":

            if "sales" in sheet_name:

                return "Revenue"

            if "purchase" in sheet_name:

                return "Purchase Cost"

            if "employee" in sheet_name:

                return "Salary"

            if "finance" in sheet_name:

                return "Amount"

            return "Business Value"

        if semantic == "Quantity":

            return "Quantity"

        if semantic == "Customer":

            return "Customer"

        if semantic == "Product":

            return "Product"

        if semantic == "Person":

            return "Employee"

        return semantic

    def business_category(self, sheet_name, column_name, semantics):

        semantic = semantics.get(column_name, "Unknown")

        if semantic in [

            "Currency",
            "Quantity"

        ]:

            return "Measure"

        return "Dimension"

    def display_name(self, business_name):

        mapping = {

            "Revenue":"Total Revenue",

            "Purchase Cost":"Total Purchase Cost",

            "Salary":"Total Payroll",

            "Business Value":"Business Value",

            "Quantity":"Total Quantity",

            "Employee":"Employee Count",

            "Customer":"Customer Count",

            "Product":"Product Count"

        }

        return mapping.get(

            business_name,

            business_name

        )