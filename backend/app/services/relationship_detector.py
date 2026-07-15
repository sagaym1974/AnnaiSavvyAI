class RelationshipDetector:

    def detect(self, workbook):

        relationships = []

        worksheets = workbook.get(
            "worksheets",
            []
        )

        for i in range(len(worksheets)):

            left_sheet = worksheets[i]

            left_columns = [

                str(c).lower().strip()

                for c in left_sheet.get(
                    "column_names",
                    []
                )

            ]

            for j in range(i + 1, len(worksheets)):

                right_sheet = worksheets[j]

                right_columns = [

                    str(c).lower().strip()

                    for c in right_sheet.get(
                        "column_names",
                        []
                    )

                ]

                matches = []

                relationship_type = "Unknown"

                confidence = 0

                for left in left_columns:

                    for right in right_columns:

                        if left == right:

                            matches.append({

                                "left_column": left,

                                "right_column": right,

                                "match_type": "Exact"

                            })

                            confidence += 10

                        elif left.endswith("_id") and right.endswith("_id"):

                            if left == right:

                                matches.append({

                                    "left_column": left,

                                    "right_column": right,

                                    "match_type": "Primary Key"

                                })

                                confidence += 20

                        elif left.replace("id", "") == right.replace("id", ""):

                            matches.append({

                                "left_column": left,

                                "right_column": right,

                                "match_type": "Possible Key"

                            })

                            confidence += 8

                if matches:

                    if any(

                        m["match_type"] == "Primary Key"

                        for m in matches

                    ):

                        relationship_type = "Primary-Key"

                    elif any(

                        m["match_type"] == "Exact"

                        for m in matches

                    ):

                        relationship_type = "Exact"

                    else:

                        relationship_type = "Possible"

                    confidence = min(

                        confidence,

                        100

                    )

                    relationships.append({

                        "from_sheet": left_sheet.get(
                            "sheet_name"
                        ),

                        "to_sheet": right_sheet.get(
                            "sheet_name"
                        ),

                        "relationship_type": relationship_type,

                        "confidence": confidence,

                        "matching_columns": matches,

                        "relationship_count": len(matches)

                    })

        relationships = sorted(

            relationships,

            key=lambda x: (

                -x["confidence"],

                -x["relationship_count"]

            )

        )

        workbook["relationships"] = relationships

        return workbook