class PatternEngine:

    def generate(self, workbook):

        for sheet in workbook.get("worksheets", []):

            patterns = []

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

                variation = maximum - minimum

                # ---------------------------------------
                # Extreme Variation
                # ---------------------------------------

                if maximum >= average * 3:

                    patterns.append({

                        "type": "Extreme Variation",

                        "column": column,

                        "severity": "critical",

                        "score": 95,

                        "message":
                        f"{column} contains extreme value variations."

                    })

                # ---------------------------------------
                # High Variation
                # ---------------------------------------

                elif maximum >= average * 2:

                    patterns.append({

                        "type": "High Variation",

                        "column": column,

                        "severity": "warning",

                        "score": 80,

                        "message":
                        f"{column} shows unusually high variation."

                    })

                # ---------------------------------------
                # Stable Pattern
                # ---------------------------------------

                elif variation <= average * 0.10:

                    patterns.append({

                        "type": "Stable Pattern",

                        "column": column,

                        "severity": "success",

                        "score": 20,

                        "message":
                        f"{column} is highly consistent."

                    })

                # ---------------------------------------
                # Normal Pattern
                # ---------------------------------------

                else:

                    patterns.append({

                        "type": "Normal Distribution",

                        "column": column,

                        "severity": "info",

                        "score": 40,

                        "message":
                        f"{column} follows a normal business distribution."

                    })

                # ---------------------------------------
                # Skewness
                # ---------------------------------------

                if median > 0:

                    ratio = abs(

                        average - median

                    ) / median

                    if ratio > 0.35:

                        patterns.append({

                            "type": "Skewed Distribution",

                            "column": column,

                            "severity": "warning",

                            "score": 65,

                            "message":
                            f"{column} distribution appears skewed."

                        })

                # ---------------------------------------
                # Low Diversity
                # ---------------------------------------

                if count > 0:

                    diversity = distinct / count

                    if diversity < 0.15:

                        patterns.append({

                            "type": "Repeated Values",

                            "column": column,

                            "severity": "info",

                            "score": 35,

                            "message":
                            f"{column} contains many repeated values."

                        })

            patterns = sorted(

                patterns,

                key=lambda x: (

                    -x["score"],

                    x["column"]

                )

            )

            sheet["patterns"] = patterns

        return workbook