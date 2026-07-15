class BusinessMeaningEngine:

    def generate(self, workbook):

        domain = workbook.get("domain", {})

        domain_name = domain.get("name", "General")

        for sheet in workbook.get("worksheets", []):

            intelligence = {}

            semantics = sheet.get("semantics", {})

            statistics = sheet.get("statistics", {})

            for column in sheet.get("column_names", []):

                semantic = semantics.get(column, "Unknown")

                business_name = self.get_business_name(

                    domain_name,

                    semantic,

                    column

                )

                intelligence[column] = {

                    "business_name": business_name,

                    "display_name": self.get_display_name(
                        business_name
                    ),

                    "business_category": self.get_category(
                        semantic
                    ),

                    "semantic": semantic,

                    "statistics": statistics.get(
                        column,
                        {}
                    )

                }

            sheet["business_meaning"] = intelligence

        return workbook

    def get_business_name(

        self,

        domain,

        semantic,

        column

    ):

        name = column.lower()

        if semantic == "Currency":

            if domain == "Sales":

                return "Revenue"

            if domain == "Finance":

                return "Financial Value"

            if domain == "HR":

                return "Payroll"

            if domain == "Inventory":

                return "Inventory Value"

            return "Business Value"

        if semantic == "Quantity":

            return "Quantity"

        if semantic == "Customer":

            return "Customer"

        if semantic == "Product":

            return "Product"

        if semantic == "Person":

            return "Employee"

        if semantic == "Date":

            return "Business Date"

        if semantic == "Location":

            return "Location"

        if semantic == "Identifier":

            return "Identifier"

        if "profit" in name:

            return "Profit"

        if "margin" in name:

            return "Margin"

        if "stock" in name:

            return "Inventory"

        return column

    def get_display_name(

        self,

        business_name

    ):

        mapping = {

            "Revenue": "Total Revenue",

            "Financial Value": "Financial Value",

            "Payroll": "Total Payroll",

            "Inventory Value": "Inventory Value",

            "Quantity": "Total Quantity",

            "Customer": "Customer Count",

            "Product": "Product Count",

            "Employee": "Employee Count",

            "Profit": "Total Profit",

            "Margin": "Average Margin",

            "Inventory": "Inventory Level"

        }

        return mapping.get(

            business_name,

            business_name

        )

    def get_category(

        self,

        semantic

    ):

        if semantic in [

            "Currency",

            "Quantity"

        ]:

            return "Measure"

        return "Dimension"