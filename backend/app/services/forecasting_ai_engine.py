class ForecastingAIEngine:

    def generate(self, workbook):

        forecasts = {}

        prediction = workbook.get(
            "predictions",
            {}
        )

        for sheet_name, sheet in prediction.items():

            ai_prediction = {}

            for metric, values in sheet.items():

                predicted = values.get(
                    "prediction",
                    0
                )

                if predicted > 0:

                    direction = "Growth"

                elif predicted < 0:

                    direction = "Decline"

                else:

                    direction = "Stable"

                ai_prediction[metric] = {

                    "prediction": predicted,

                    "direction": direction,

                    "confidence":

                        values.get(
                            "confidence",
                            0
                        )

                }

            forecasts[sheet_name] = ai_prediction

        workbook["forecast_ai"] = forecasts

        return workbook