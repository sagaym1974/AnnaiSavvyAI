class MetadataEngine:

    def generate(self, workbook):

        for sheet in workbook.get("worksheets", []):

            metadata = {}

            columns = sheet.get(
                "column_names",
                []
            )

            numeric_columns = sheet.get(
                "numeric_columns",
                []
            )

            date_columns = sheet.get(
                "date_columns",
                []
            )

            semantics = sheet.get(
                "semantics",
                {}
            )

            statistics = sheet.get(
                "statistics",
                {}
            )

            for column in columns:

                meta = {}

                semantic = semantics.get(
                    column,
                    "Unknown"
                )

                is_numeric = column in numeric_columns

                is_date = column in date_columns

                stats = statistics.get(
                    column,
                    {}
                )

                distinct = stats.get(
                    "distinct",
                    0
                )

                count = stats.get(
                    "count",
                    0
                )

                uniqueness = 0

                if count > 0:

                    uniqueness = round(

                        (distinct / count) * 100,

                        2

                    )

                # -----------------------------------------
                # Basic Information
                # -----------------------------------------

                meta["name"] = column

                meta["semantic"] = semantic

                meta["is_numeric"] = is_numeric

                meta["is_date"] = is_date

                meta["is_text"] = (

                    not is_numeric

                    and

                    not is_date

                )

                meta["is_dimension"] = (

                    not is_numeric

                )

                meta["is_measure"] = (

                    is_numeric

                )

                # -----------------------------------------
                # BI Usage
                # -----------------------------------------

                meta["usable_for_chart"] = True

                meta["usable_for_filter"] = True

                meta["usable_for_groupby"] = (

                    not is_numeric

                )

                meta["usable_for_kpi"] = (

                    is_numeric

                )

                meta["usable_for_sorting"] = True

                meta["usable_for_search"] = (

                    not is_numeric

                )

                # -----------------------------------------
                # Statistics
                # -----------------------------------------

                meta["record_count"] = count

                meta["distinct_values"] = distinct

                meta["uniqueness"] = uniqueness

                # -----------------------------------------
                # AI Intelligence
                # -----------------------------------------

                intelligence = 100

                if semantic == "Unknown":

                    intelligence -= 15

                if not meta["usable_for_chart"]:

                    intelligence -= 10

                if not meta["usable_for_kpi"]:

                    intelligence -= 10

                if uniqueness < 5:

                    intelligence -= 20

                intelligence = max(

                    intelligence,

                    0

                )

                meta["ai_score"] = intelligence

                meta["ai_status"] = (

                    "Excellent"

                    if intelligence >= 90 else

                    "Good"

                    if intelligence >= 75 else

                    "Average"

                    if intelligence >= 60 else

                    "Poor"

                )

                metadata[column] = meta

            sheet["metadata"] = metadata

        return workbook