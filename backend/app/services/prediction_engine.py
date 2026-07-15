class PredictionEngine:

    def generate(self, workbook):

        predictions = {}

        forecast = workbook.get(
            "forecast",
            {}
        )

        for sheet_name, sheet in forecast.items():

            prediction = {}

            for metric, values in sheet.items():

                next_value = values.get(
                    "next_period",
                    0
                )

                optimistic = values.get(
                    "optimistic",
                    0
                )

                conservative = values.get(
                    "conservative",
                    0
                )

                confidence = round(

                    (

                        optimistic +

                        conservative

                    ) / 2,

                    2

                )

                prediction[metric] = {

                    "prediction":

                        next_value,

                    "confidence":

                        confidence,

                    "range":

                        values.get(
                            "expected_range",
                            []
                        )

                }

            predictions[sheet_name] = prediction

        workbook["predictions"] = predictions

        return workbook