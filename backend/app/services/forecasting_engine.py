class ForecastingEngine:

    def generate(self, workbook):

        forecast = {}

        for sheet in workbook.get(
            "worksheets",
            []
        ):

            sheet_name = sheet["sheet_name"]

            statistics = sheet.get(
                "statistics",
                {}
            )

            prediction = {}

            for column, stats in statistics.items():

                average = stats.get(
                    "average",
                    0
                )

                maximum = stats.get(
                    "maximum",
                    0
                )

                minimum = stats.get(
                    "minimum",
                    0
                )

                projected_growth = average * 1.10

                optimistic = maximum * 1.05

                conservative = average * 0.95

                prediction[column] = {

                    "next_period":

                        round(
                            projected_growth,
                            2
                        ),

                    "optimistic":

                        round(
                            optimistic,
                            2
                        ),

                    "conservative":

                        round(
                            conservative,
                            2
                        ),

                    "expected_range":

                        [

                            round(minimum, 2),

                            round(maximum, 2)

                        ]

                }

            forecast[sheet_name] = prediction

        workbook["forecast"] = forecast

        return workbook