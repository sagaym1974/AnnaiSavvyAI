class OpportunityEngine:

    def generate(self, workbook):

        opportunities = []

        aggregation = workbook.get(
            "aggregation",
            {}
        )

        for sheet_name, sheet in aggregation.items():

            for dimension, measures in sheet.items():

                for measure, values in measures.items():

                    top = values.get(
                        "top_10",
                        []
                    )

                    if len(top) < 2:

                        continue

                    leader = top[0]

                    opportunities.append({

                        "sheet": sheet_name,

                        "dimension": dimension,

                        "measure": measure,

                        "title":

                            f"Top {dimension}",

                        "message":

                            f"{leader[0]} contributes the highest {measure} ({round(leader[1],2)}).",

                        "priority": "Medium"

                    })

        workbook["opportunities"] = opportunities

        return workbook