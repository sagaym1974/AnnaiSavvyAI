class DataQualityEngine:

    def generate(self, workbook):

        quality = {}

        total_rows = 0
        total_columns = 0

        missing_values = 0
        duplicate_rows = 0
        empty_columns = 0

        complete_rows = 0

        numeric_columns = 0
        text_columns = 0
        date_columns = 0

        for sheet in workbook.get("worksheets", []):

            sample = sheet.get(
                "sample_data",
                []
            )

            columns = sheet.get(
                "column_names",
                []
            )

            total_rows += len(sample)
            total_columns += len(columns)

            numeric_columns += len(
                sheet.get(
                    "numeric_columns",
                    []
                )
            )

            date_columns += len(
                sheet.get(
                    "date_columns",
                    []
                )
            )

            text_columns += (

                len(columns)

                -

                len(sheet.get("numeric_columns", []))

            )

            seen = set()

            for row in sample:

                row_key = tuple(

                    sorted(row.items())

                )

                if row_key in seen:

                    duplicate_rows += 1

                else:

                    seen.add(row_key)

                row_complete = True

                for value in row.values():

                    if (

                        value is None

                        or

                        str(value).strip() == ""

                    ):

                        missing_values += 1
                        row_complete = False

                if row_complete:

                    complete_rows += 1

            for column in columns:

                values = [

                    row.get(column)

                    for row in sample

                ]

                if all(

                    v is None

                    or

                    str(v).strip() == ""

                    for v in values

                ):

                    empty_columns += 1

        # ---------------------------------------------
        # Quality Score
        # ---------------------------------------------

        score = 100

        score -= duplicate_rows * 5

        score -= missing_values

        score -= empty_columns * 5

        if score < 0:

            score = 0

        completeness = 100

        if total_rows > 0:

            completeness = round(

                (

                    complete_rows /

                    total_rows

                ) * 100,

                2

            )

        uniqueness = 100

        if total_rows > 0:

            uniqueness = round(

                (

                    (

                        total_rows -

                        duplicate_rows

                    ) /

                    total_rows

                ) * 100,

                2

            )

        quality["score"] = score

        quality["status"] = (

            "Excellent"

            if score >= 95 else

            "Very Good"

            if score >= 85 else

            "Good"

            if score >= 70 else

            "Average"

            if score >= 50 else

            "Poor"

        )

        quality["rows"] = total_rows

        quality["columns"] = total_columns

        quality["duplicates"] = duplicate_rows

        quality["missing"] = missing_values

        quality["empty_columns"] = empty_columns

        quality["completeness"] = completeness

        quality["uniqueness"] = uniqueness

        quality["numeric_columns"] = numeric_columns

        quality["text_columns"] = text_columns

        quality["date_columns"] = date_columns

        workbook["data_quality"] = quality

        return workbook