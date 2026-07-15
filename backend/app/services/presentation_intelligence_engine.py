from datetime import datetime


class PresentationIntelligenceEngine:

    def generate(self, workbook):

        for sheet in workbook.get("worksheets", []):

            sample_data = sheet.get(
                "sample_data",
                []
            )

            date_columns = sheet.get(
                "date_columns",
                []
            )

            numeric_columns = sheet.get(
                "numeric_columns",
                []
            )

            presentation_data = []

            for row in sample_data:

                new_row = {}

                for column, value in row.items():

                    if column in date_columns:

                        new_row[column] = self.format_date(

                            value,

                            sample_data,

                            column

                        )

                    elif column in numeric_columns:

                        new_row[column] = self.format_number(

                            value

                        )

                    else:

                        new_row[column] = value

                presentation_data.append(new_row)

            sheet["presentation_data"] = presentation_data

        return workbook

    # --------------------------------------------------
    # DATE FORMATTING
    # --------------------------------------------------

    def format_date(

        self,

        value,

        rows,

        column

    ):

        dt = self.parse_date(value)

        if dt is None:

            return value

        dates = []

        for row in rows:

            parsed = self.parse_date(

                row.get(column)

            )

            if parsed:

                dates.append(parsed)

        if len(dates) < 2:

            return dt.strftime("%d %b %Y")

        minimum = min(dates)

        maximum = max(dates)

        span = (maximum - minimum).days

        if span > 3650:

            return dt.strftime("%Y")

        if span > 365:

            return dt.strftime("%b %Y")

        if span > 90:

            return dt.strftime("%d %b")

        if span > 1:

            return dt.strftime("%d %b")

        return dt.strftime("%H:%M")

    # --------------------------------------------------
    # NUMBER FORMATTING
    # --------------------------------------------------

    def format_number(

        self,

        value

    ):

        try:

            value = float(value)

        except:

            return value

        absolute = abs(value)

        if absolute >= 1_000_000_000:

            return f"{value/1_000_000_000:.2f} B"

        if absolute >= 1_000_000:

            return f"{value/1_000_000:.2f} M"

        if absolute >= 1_000:

            return f"{value/1_000:.2f} K"

        if absolute >= 100:

            return f"{value:,.2f}"

        if value.is_integer():

            return int(value)

        return round(value, 2)

    # --------------------------------------------------
    # DATE PARSER
    # --------------------------------------------------

    def parse_date(

        self,

        value

    ):

        if value is None:

            return None

        if isinstance(

            value,

            datetime

        ):

            return value

        try:

            return datetime.fromisoformat(

                str(value)

            )

        except:

            pass

        formats = [

            "%Y-%m-%d",

            "%Y/%m/%d",

            "%d/%m/%Y",

            "%m/%d/%Y",

            "%d-%m-%Y",

            "%Y-%m-%d %H:%M:%S",

            "%Y/%m/%d %H:%M:%S",

            "%d/%m/%Y %H:%M:%S",

            "%m/%d/%Y %H:%M:%S",

            "%Y-%m-%dT%H:%M:%S",

            "%d-%b-%Y",

            "%d %b %Y",

            "%b %d %Y"

        ]

        for fmt in formats:

            try:

                return datetime.strptime(

                    str(value),

                    fmt

                )

            except:

                pass

        return None