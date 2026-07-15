class ColumnIntelligenceEngine:

    def generate(self, workbook):

        for sheet in workbook.get("worksheets", []):

            columns = {}

            metadata = sheet.get(
                "metadata",
                {}
            )

            semantics = sheet.get(
                "semantics",
                {}
            )

            statistics = sheet.get(
                "statistics",
                {}
            )

            business_meaning = sheet.get(
                "business_meaning",
                {}
            )

            numeric_columns = sheet.get(
                "numeric_columns",
                []
            )

            date_columns = sheet.get(
                "date_columns",
                []
            )

            patterns = sheet.get(
                "patterns",
                []
            )

            anomalies = workbook.get(
                "anomalies",
                []
            )

            for column in sheet.get("column_names", []):

                info = {}

                # --------------------------------------------------
                # Basic Information
                # --------------------------------------------------

                info["name"] = column

                if column in date_columns:

                    datatype = "Date"

                elif column in numeric_columns:

                    datatype = "Numeric"

                else:

                    datatype = "Text"

                info["datatype"] = datatype

                info["semantic"] = semantics.get(

                    column,

                    "Unknown"

                )

                info["role"] = (

                    "Measure"

                    if column in numeric_columns

                    else "Dimension"

                )

                # --------------------------------------------------
                # Business Intelligence
                # --------------------------------------------------

                business = business_meaning.get(

                    column,

                    {}

                )

                info["business_name"] = business.get(

                    "business_name",

                    column

                )

                info["display_name"] = business.get(

                    "display_name",

                    column

                )

                info["business_category"] = business.get(

                    "business_category",

                    "Unknown"

                )

                # --------------------------------------------------
                # Statistics
                # --------------------------------------------------

                info["statistics"] = statistics.get(

                    column,

                    {}

                )

                # --------------------------------------------------
                # Visualization
                # --------------------------------------------------

                meta = metadata.get(

                    column,

                    {}

                )

                info["chart"] = meta.get(

                    "usable_for_chart",

                    False

                )

                info["kpi"] = meta.get(

                    "usable_for_kpi",

                    False

                )

                info["filter"] = meta.get(

                    "usable_for_filter",

                    False

                )

                info["groupby"] = meta.get(

                    "usable_for_groupby",

                    False

                )

                # --------------------------------------------------
                # Pattern Intelligence
                # --------------------------------------------------

                info["patterns"] = [

                    p

                    for p in patterns

                    if p.get("column") == column

                ]

                # --------------------------------------------------
                # Anomaly Intelligence
                # --------------------------------------------------

                info["anomalies"] = [

                    a

                    for a in anomalies

                    if

                    a.get("sheet") == sheet["sheet_name"]

                    and

                    a.get("column") == column

                ]

                # --------------------------------------------------
                # AI Readiness
                # --------------------------------------------------

                readiness = 100

                if not info["chart"]:

                    readiness -= 20

                if not info["kpi"]:

                    readiness -= 20

                if datatype == "Text":

                    readiness -= 15

                readiness = max(

                    readiness,

                    0

                )

                info["ai_readiness"] = readiness

                info["ai_status"] = (

                    "Excellent"

                    if readiness >= 90 else

                    "Good"

                    if readiness >= 75 else

                    "Average"

                    if readiness >= 60 else

                    "Poor"

                )

                columns[column] = info

            sheet["column_intelligence"] = columns

        return workbook