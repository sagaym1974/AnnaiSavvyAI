class RelationshipDetector:

    def detect(self, workbook):

        relationships = []

        worksheets = workbook["worksheets"]

        for i in range(len(worksheets)):

            left_sheet = worksheets[i]

            left_columns = left_sheet["column_names"]

            for j in range(i + 1, len(worksheets)):

                right_sheet = worksheets[j]

                right_columns = right_sheet["column_names"]

                common = list(
                    set(left_columns).intersection(right_columns)
                )

                if common:

                    relationships.append(
                        {
                            "from_sheet": left_sheet["sheet_name"],
                            "to_sheet": right_sheet["sheet_name"],
                            "matching_columns": common
                        }
                    )

        workbook["relationships"] = relationships

        return workbook