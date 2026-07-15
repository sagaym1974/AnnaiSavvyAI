class AggregationEngine:

    def generate(self, workbook):

        aggregation = {}

        for sheet in workbook.get("worksheets", []):

            sheet_name = sheet.get(
                "sheet_name",
                "Unknown"
            )

            sample_data = sheet.get(
                "sample_data",
                []
            )

            meanings = sheet.get(
                "business_meaning",
                {}
            )

            sheet_result = {}

            # --------------------------------------------
            # Detect Measures & Dimensions
            # --------------------------------------------

            measures = []

            dimensions = []

            for column, info in meanings.items():

                if info.get("business_category") == "Measure":

                    measures.append(column)

                else:

                    dimensions.append(column)

            # --------------------------------------------
            # Aggregate
            # --------------------------------------------

            for dimension in dimensions:

                sheet_result[dimension] = {}

                for measure in measures:

                    grouped = {}

                    for row in sample_data:

                        key = row.get(dimension)

                        value = row.get(measure)

                        if key in [None, ""]:

                            key = "Unknown"

                        try:

                            value = float(value)

                        except:

                            continue

                        grouped.setdefault(key, 0)

                        grouped[key] += value

                    grouped = dict(

                        sorted(

                            grouped.items(),

                            key=lambda x: x[1],

                            reverse=True

                        )

                    )

                    sheet_result[dimension][measure] = {

                        "group_count": len(grouped),

                        "total": round(

                            sum(grouped.values()),

                            2

                        ),

                        "top_10": list(grouped.items())[:10],

                        "bottom_10": list(grouped.items())[-10:]

                    }

            aggregation[sheet_name] = sheet_result

        workbook["aggregation"] = aggregation

        return workbook