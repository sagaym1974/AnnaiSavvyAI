class BenchmarkingEngine:

    def generate(self, workbook):

        benchmark = {}

        for sheet in workbook.get("worksheets", []):

            sheet_name = sheet["sheet_name"]

            statistics = sheet.get(
                "statistics",
                {}
            )

            result = {}

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

                if average == 0:

                    continue

                score = (

                    average / maximum

                ) * 100

                if score >= 90:

                    rating = "Excellent"

                elif score >= 75:

                    rating = "Good"

                elif score >= 60:

                    rating = "Average"

                else:

                    rating = "Poor"

                result[column] = {

                    "benchmark_score":

                        round(score, 2),

                    "rating":

                        rating,

                    "industry_best":

                        round(maximum, 2),

                    "industry_average":

                        round(average, 2),

                    "industry_low":

                        round(minimum, 2)

                }

            benchmark[sheet_name] = result

        workbook["benchmarking"] = benchmark

        return workbook