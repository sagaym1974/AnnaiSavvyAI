class AnomalyEngine:

    def generate(self, workbook):

        anomalies = []

        for sheet in workbook.get("worksheets", []):

            statistics = sheet.get(
                "statistics",
                {}
            )

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

                median = stats.get(
                    "median",
                    0
                )

                distinct = stats.get(
                    "distinct",
                    0
                )

                count = stats.get(
                    "count",
                    0
                )

                if average <= 0:

                    continue

                # -----------------------------------------
                # High Outlier
                # -----------------------------------------

                if maximum >= average * 3:

                    anomalies.append({

                        "sheet": sheet["sheet_name"],

                        "column": column,

                        "severity": "Critical",

                        "type": "Extreme High Value",

                        "score": 95,

                        "message":
                        f"The maximum value of '{column}' is significantly higher than the business average."

                    })

                # -----------------------------------------
                # Low Outlier
                # -----------------------------------------

                if minimum <= average * 0.10:

                    anomalies.append({

                        "sheet": sheet["sheet_name"],

                        "column": column,

                        "severity": "High",

                        "type": "Extreme Low Value",

                        "score": 80,

                        "message":
                        f"Very low values were detected in '{column}'. Review possible data or business issues."

                    })

                # -----------------------------------------
                # Distribution Check
                # -----------------------------------------

                if median > 0:

                    ratio = abs(average - median) / median

                    if ratio > 0.40:

                        anomalies.append({

                            "sheet": sheet["sheet_name"],

                            "column": column,

                            "severity": "Medium",

                            "type": "Distribution Variation",

                            "score": 60,

                            "message":
                            f"'{column}' shows uneven value distribution and possible skewness."

                        })

                # -----------------------------------------
                # Low Diversity
                # -----------------------------------------

                if count > 0:

                    diversity = distinct / count

                    if diversity < 0.10:

                        anomalies.append({

                            "sheet": sheet["sheet_name"],

                            "column": column,

                            "severity": "Low",

                            "type": "Low Diversity",

                            "score": 35,

                            "message":
                            f"'{column}' contains many repeated values."

                        })

        anomalies = sorted(

            anomalies,

            key=lambda x: (

                -x["score"],

                x["sheet"]

            )

        )

        workbook["anomalies"] = anomalies

        return workbook