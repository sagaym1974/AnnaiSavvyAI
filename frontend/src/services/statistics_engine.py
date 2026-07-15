from statistics import median, mode, StatisticsError


class StatisticsEngine:

    def generate(self, workbook):

        for sheet in workbook["worksheets"]:

            statistics = {}

            numeric_columns = sheet.get("numeric_columns", [])

            sample_data = sheet.get("sample_data", [])

            for column in numeric_columns:

                values = []

                for row in sample_data:

                    value = row.get(column)

                    if isinstance(value, (int, float)):

                        values.append(value)

                if len(values) == 0:

                    continue

                try:
                    mode_value = mode(values)
                except StatisticsError:
                    mode_value = None

                statistics[column] = {

                    "count": len(values),

                    "sum": sum(values),

                    "minimum": min(values),

                    "maximum": max(values),

                    "average": round(sum(values) / len(values), 2),

                    "median": median(values),

                    "mode": mode_value,

                    "distinct": len(set(values))

                }

            sheet["statistics"] = statistics

        return workbook