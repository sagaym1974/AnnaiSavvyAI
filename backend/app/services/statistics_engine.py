from numbers import Number
from statistics import median


class StatisticsEngine:

    def generate(self, workbook):

        for sheet in workbook["worksheets"]:

            statistics = {}

            sample_data = sheet.get("sample_data", [])

            for column in sheet.get("numeric_columns", []):

                values = []

                for row in sample_data:

                    value = row.get(column)

                    if isinstance(value, Number) and not isinstance(value, bool):

                        values.append(float(value))

                if not values:

                    continue

                statistics[column] = {

                    "count": len(values),
                    "sum": round(sum(values), 2),
                    "minimum": min(values),
                    "maximum": max(values),
                    "average": round(sum(values) / len(values), 2),
                    "median": median(values),
                    "distinct": len(set(values))

                }

            sheet["statistics"] = statistics

        return workbook