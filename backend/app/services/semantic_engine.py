class SemanticEngine:

    def generate(self, workbook):

        for sheet in workbook.get("worksheets", []):

            semantics = {}

            for column in sheet.get("column_names", []):

                name = str(column).lower().strip()

                semantic = "Text"

                # ------------------------------------------------
                # Currency
                # ------------------------------------------------

                if any(word in name for word in [

                    "amount",
                    "amt",
                    "price",
                    "cost",
                    "salary",
                    "income",
                    "expense",
                    "revenue",
                    "sales",
                    "profit",
                    "margin",
                    "balance",
                    "payment",
                    "credit",
                    "debit",
                    "commission",
                    "tax",
                    "gst",
                    "cgst",
                    "sgst",
                    "igst",
                    "discount",
                    "net",
                    "gross",
                    "value"

                ]):

                    semantic = "Currency"

                # ------------------------------------------------
                # Quantity
                # ------------------------------------------------

                elif any(word in name for word in [

                    "qty",
                    "quantity",
                    "stock",
                    "inventory",
                    "units",
                    "pieces",
                    "volume",
                    "weight",
                    "count"

                ]):

                    semantic = "Quantity"

                # ------------------------------------------------
                # Date
                # ------------------------------------------------

                elif any(word in name for word in [

                    "date",
                    "month",
                    "year",
                    "week",
                    "day",
                    "time",
                    "created",
                    "updated",
                    "invoice date",
                    "order date"

                ]):

                    semantic = "Date"

                # ------------------------------------------------
                # Customer
                # ------------------------------------------------

                elif any(word in name for word in [

                    "customer",
                    "client",
                    "buyer"

                ]):

                    semantic = "Customer"

                # ------------------------------------------------
                # Product
                # ------------------------------------------------

                elif any(word in name for word in [

                    "product",
                    "item",
                    "material",
                    "sku",
                    "brand",
                    "model"

                ]):

                    semantic = "Product"

                # ------------------------------------------------
                # Employee
                # ------------------------------------------------

                elif any(word in name for word in [

                    "employee",
                    "staff",
                    "emp",
                    "person",
                    "associate"

                ]):

                    semantic = "Person"

                # ------------------------------------------------
                # Name
                # ------------------------------------------------

                elif any(word in name for word in [

                    "name",
                    "fullname",
                    "full name"

                ]):

                    semantic = "Name"

                # ------------------------------------------------
                # Department
                # ------------------------------------------------

                elif any(word in name for word in [

                    "department",
                    "dept",
                    "division"

                ]):

                    semantic = "Department"

                # ------------------------------------------------
                # Designation
                # ------------------------------------------------

                elif any(word in name for word in [

                    "designation",
                    "role",
                    "position",
                    "title"

                ]):

                    semantic = "Designation"

                # ------------------------------------------------
                # Vendor
                # ------------------------------------------------

                elif any(word in name for word in [

                    "vendor",
                    "supplier"

                ]):

                    semantic = "Vendor"

                # ------------------------------------------------
                # Location
                # ------------------------------------------------

                elif any(word in name for word in [

                    "city",
                    "state",
                    "country",
                    "region",
                    "territory",
                    "location",
                    "branch"

                ]):

                    semantic = "Location"

                # ------------------------------------------------
                # Email
                # ------------------------------------------------

                elif any(word in name for word in [

                    "email",
                    "mail"

                ]):

                    semantic = "Email"

                # ------------------------------------------------
                # Phone
                # ------------------------------------------------

                elif any(word in name for word in [

                    "phone",
                    "mobile",
                    "telephone",
                    "contact"

                ]):

                    semantic = "Phone"

                # ------------------------------------------------
                # Identifier
                # ------------------------------------------------

                elif any(word in name for word in [

                    "id",
                    "code",
                    "number",
                    "no",
                    "serial",
                    "reference",
                    "ref"

                ]):

                    semantic = "Identifier"

                # ------------------------------------------------
                # Project
                # ------------------------------------------------

                elif any(word in name for word in [

                    "project",
                    "task",
                    "activity"

                ]):

                    semantic = "Project"

                # ------------------------------------------------
                # Status
                # ------------------------------------------------

                elif any(word in name for word in [

                    "status",
                    "stage"

                ]):

                    semantic = "Status"

                semantics[column] = semantic

            sheet["semantics"] = semantics

        return workbook