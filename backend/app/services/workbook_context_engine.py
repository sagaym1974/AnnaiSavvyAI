from collections import Counter


class WorkbookContextEngine:

    def generate(self, workbook):

        context = {

            "worksheet_count": 0,

            "column_count": 0,

            "row_count": 0,

            "numeric_column_count": 0,

            "text_column_count": 0,

            "date_column_count": 0,

            "numeric_columns": [],

            "text_columns": [],

            "date_columns": [],

            "worksheet_names": [],

            "semantic_frequency": {},

            "dataset_types": [],

            "dominant_dataset": "Unknown",

            "largest_sheet": "",

            "largest_sheet_rows": 0,

            "average_rows_per_sheet": 0,

            "average_columns_per_sheet": 0

        }

        semantic_counter = Counter()

        dataset_counter = Counter()

        worksheets = workbook.get(

            "worksheets",

            []

        )

        context["worksheet_count"] = len(

            worksheets

        )

        for sheet in worksheets:

            sheet_name = sheet.get(

                "sheet_name",

                "Unknown"

            )

            context["worksheet_names"].append(

                sheet_name

            )

            rows = sheet.get(

                "rows",

                len(

                    sheet.get(

                        "sample_data",

                        []

                    )

                )

            )

            columns = sheet.get(

                "column_names",

                []

            )

            context["row_count"] += rows

            context["column_count"] += len(

                columns

            )

            if rows > context["largest_sheet_rows"]:

                context["largest_sheet_rows"] = rows

                context["largest_sheet"] = sheet_name

            dataset = sheet.get(

                "dataset_type",

                "Unknown"

            )

            context["dataset_types"].append(

                dataset

            )

            dataset_counter.update(

                [dataset]

            )

            numeric = sheet.get(

                "numeric_columns",

                []

            )

            dates = sheet.get(

                "date_columns",

                []

            )

            context["numeric_columns"].extend(

                numeric

            )

            context["date_columns"].extend(

                dates

            )

            for column in columns:

                if (

                    column not in numeric

                    and

                    column not in dates

                ):

                    context["text_columns"].append(

                        column

                    )

            semantics = sheet.get(

                "semantics",

                {}

            )

            semantic_counter.update(

                semantics.values()

            )

        context["numeric_column_count"] = len(

            context["numeric_columns"]

        )

        context["text_column_count"] = len(

            context["text_columns"]

        )

        context["date_column_count"] = len(

            context["date_columns"]

        )

        if context["worksheet_count"] > 0:

            context["average_rows_per_sheet"] = round(

                context["row_count"] /

                context["worksheet_count"],

                2

            )

            context["average_columns_per_sheet"] = round(

                context["column_count"] /

                context["worksheet_count"],

                2

            )

        if dataset_counter:

            context["dominant_dataset"] = dataset_counter.most_common(

                1

            )[0][0]

        context["semantic_frequency"] = dict(

            semantic_counter

        )

        workbook["workbook_context"] = context

        return workbook