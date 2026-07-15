import pandas as pd

from app.models.workbook_model import WorkbookModel


def read_excel_workbook(file, filename):

    excel = pd.ExcelFile(file)

    workbook = WorkbookModel(filename)

    for sheet_name in excel.sheet_names:

        df = pd.read_excel(

            excel,

            sheet_name=sheet_name

        )

        # -----------------------------------------
        # Clean Column Names
        # -----------------------------------------

        df.columns = [

            str(col).strip()

            for col in df.columns

        ]

        # -----------------------------------------
        # Remove Fully Empty Rows
        # -----------------------------------------

        df = df.dropna(

            how="all"

        )

        # -----------------------------------------
        # Remove Fully Empty Columns
        # -----------------------------------------

        df = df.dropna(

            axis=1,

            how="all"

        )

        # -----------------------------------------
        # Replace NaN
        # -----------------------------------------

        cleaned = df.fillna("")

        # -----------------------------------------
        # Sample Data
        # -----------------------------------------

        sample_size = min(

            100,

            len(cleaned)

        )

        sample = cleaned.head(

            sample_size

        ).to_dict(

            orient="records"

        )

        # -----------------------------------------
        # Data Types
        # -----------------------------------------

        data_types = {

            column: str(dtype)

            for column, dtype

            in cleaned.dtypes.items()

        }

        # -----------------------------------------
        # Workbook Sheet
        # -----------------------------------------

        workbook.add_sheet({

            "sheet_name": sheet_name,

            "rows": len(cleaned),

            "columns": len(cleaned.columns),

            "column_names": list(cleaned.columns),

            "data_types": data_types,

            "sample_data": sample

        })

    return workbook.build()