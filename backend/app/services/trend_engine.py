class TrendEngine:

    def generate(self, workbook):

        trends = {}

        aggregation = workbook.get(
            "aggregation",
            {}
        )

        for sheet_name, sheet_data in aggregation.items():

            sheet_trends = {}

            for dimension, measures in sheet_data.items():

                sheet_trends[dimension] = {}

                for measure, values in measures.items():

                    top = values.get(
                        "top_10",
                        []
                    )

                    if len(top) < 2:

                        continue

                    trend = {}

                    highest = top[0][1]

                    lowest = top[-1][1]

                    if highest > lowest * 2:

                        strength = "Strong"

                    elif highest > lowest * 1.3:

                        strength = "Moderate"

                    else:

                        strength = "Stable"

                    average = sum(

                        value

                        for _, value in top

                    ) / len(top)

                    trend["strength"] = strength

                    trend["average"] = round(
                        average,
                        2
                    )

                    trend["highest"] = {

                        "name": top[0][0],

                        "value": round(
                            top[0][1],
                            2
                        )

                    }

                    trend["lowest"] = {

                        "name": top[-1][0],

                        "value": round(
                            top[-1][1],
                            2
                        )

                    }

                    trend["distribution"] = top

                    sheet_trends[dimension][measure] = trend

            trends[sheet_name] = sheet_trends

        workbook["trends"] = trends

        return workbook