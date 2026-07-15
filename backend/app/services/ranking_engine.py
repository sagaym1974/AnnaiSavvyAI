class RankingEngine:

    def generate(self, workbook):

        rankings = {}

        aggregation = workbook.get(
            "aggregation",
            {}
        )

        for sheet_name, sheet_data in aggregation.items():

            sheet_rankings = {}

            for dimension, measures in sheet_data.items():

                sheet_rankings[dimension] = {}

                for measure, values in measures.items():

                    top = values.get(
                        "top_10",
                        []
                    )

                    bottom = values.get(
                        "bottom_10",
                        []
                    )

                    ranking = {

                        "leader": None,

                        "runner_up": None,

                        "third": None,

                        "bottom": None,

                        "top_10": top,

                        "bottom_10": bottom

                    }

                    if len(top) >= 1:

                        ranking["leader"] = {

                            "name": top[0][0],

                            "value": round(top[0][1], 2)

                        }

                    if len(top) >= 2:

                        ranking["runner_up"] = {

                            "name": top[1][0],

                            "value": round(top[1][1], 2)

                        }

                    if len(top) >= 3:

                        ranking["third"] = {

                            "name": top[2][0],

                            "value": round(top[2][1], 2)

                        }

                    if len(bottom) >= 1:

                        ranking["bottom"] = {

                            "name": bottom[0][0],

                            "value": round(bottom[0][1], 2)

                        }

                    sheet_rankings[dimension][measure] = ranking

            rankings[sheet_name] = sheet_rankings

        workbook["ranking"] = rankings

        return workbook