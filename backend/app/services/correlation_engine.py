from itertools import combinations


class CorrelationEngine:

    def generate(self, workbook):

        correlations = {}

        for sheet in workbook.get("worksheets", []):

            sheet_name = sheet["sheet_name"]

            rows = sheet.get(
                "sample_data",
                []
            )

            numeric = sheet.get(
                "numeric_columns",
                []
            )

            results = []

            for left, right in combinations(
                numeric,
                2
            ):

                left_values = []
                right_values = []

                for row in rows:

                    try:

                        x = float(row[left])
                        y = float(row[right])

                        left_values.append(x)
                        right_values.append(y)

                    except:

                        continue

                if len(left_values) < 2:

                    continue

                avg_x = sum(left_values) / len(left_values)
                avg_y = sum(right_values) / len(right_values)

                numerator = 0
                denominator_x = 0
                denominator_y = 0

                for x, y in zip(
                    left_values,
                    right_values
                ):

                    numerator += (x - avg_x) * (y - avg_y)

                    denominator_x += (x - avg_x) ** 2

                    denominator_y += (y - avg_y) ** 2

                if denominator_x == 0 or denominator_y == 0:

                    coefficient = 0

                else:

                    coefficient = numerator / (

                        (denominator_x ** 0.5)

                        *

                        (denominator_y ** 0.5)

                    )

                if abs(coefficient) >= 0.80:

                    relation = "Very Strong"

                elif abs(coefficient) >= 0.60:

                    relation = "Strong"

                elif abs(coefficient) >= 0.40:

                    relation = "Moderate"

                else:

                    relation = "Weak"

                results.append({

                    "column_x": left,

                    "column_y": right,

                    "correlation": round(
                        coefficient,
                        3
                    ),

                    "strength": relation

                })

            correlations[sheet_name] = results

        workbook["correlations"] = correlations

        return workbook