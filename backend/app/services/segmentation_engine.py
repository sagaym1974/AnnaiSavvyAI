class SegmentationEngine:

    def generate(self, workbook):

        segments = {}

        for sheet in workbook.get("worksheets", []):

            sheet_name = sheet.get(
                "sheet_name",
                "Unknown"
            )

            meanings = sheet.get(
                "business_meaning",
                {}
            )

            sample_data = sheet.get(
                "sample_data",
                []
            )

            sheet_segments = {}

            for column, info in meanings.items():

                if info.get("business_category") == "Measure":

                    continue

                frequency = {}

                for row in sample_data:

                    value = row.get(column)

                    if value in [None, ""]:

                        value = "Unknown"

                    frequency[value] = frequency.get(
                        value,
                        0
                    ) + 1

                ordered = sorted(

                    frequency.items(),

                    key=lambda x: x[1],

                    reverse=True

                )

                sheet_segments[column] = {

                    "unique_values": len(frequency),

                    "largest_segment":

                        ordered[0]

                        if ordered else None,

                    "top_segments":

                        ordered[:10]

                }

            segments[sheet_name] = sheet_segments

        workbook["segments"] = segments

        return workbook 