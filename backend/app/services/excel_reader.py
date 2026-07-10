import pandas as pd

from app.models.workbook_model import WorkbookModel


def read_excel_workbook(file, filename):

    excel = pd.ExcelFile(file)

    workbook = WorkbookModel(filename)

    for sheet_name in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name=sheet_name)

        workbook.add_sheet(
            {
                "sheet_name": sheet_name,
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns),
                "sample_data": df.head(5).fillna("").to_dict(
                    orient="records"
                )
            }
        )

    return workbook.build()