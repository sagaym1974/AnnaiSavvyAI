class RiskEngine:

    def generate(self, workbook):

        risks = []

        anomalies = workbook.get(
            "anomalies",
            []
        )

        quality = workbook.get(
            "data_quality",
            {}
        )

        for anomaly in anomalies:

            risks.append({

                "severity":

                    anomaly.get(
                        "severity",
                        "Medium"
                    ),

                "sheet":

                    anomaly.get(
                        "sheet"
                    ),

                "column":

                    anomaly.get(
                        "column"
                    ),

                "message":

                    anomaly.get(
                        "message"
                    )

            })

        if quality.get("duplicates", 0) > 0:

            risks.append({

                "severity": "Medium",

                "sheet": "Workbook",

                "column": "Duplicates",

                "message":

                    f"{quality.get('duplicates')} duplicate records detected."

            })

        if quality.get("missing", 0) > 0:

            risks.append({

                "severity": "Medium",

                "sheet": "Workbook",

                "column": "Missing Values",

                "message":

                    f"{quality.get('missing')} missing values detected."

            })

        workbook["risks"] = risks

        return workbook