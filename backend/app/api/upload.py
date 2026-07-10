from fastapi import APIRouter, UploadFile, File

from app.services.excel_reader import read_excel_workbook
from app.services.dataset_analyzer import DatasetAnalyzer

router = APIRouter()

analyzer = DatasetAnalyzer()


@router.post("/upload")
async def upload_excel(file: UploadFile = File(...)):

    workbook = read_excel_workbook(

        file.file,

        file.filename

    )

    workbook = analyzer.analyze(workbook)

    return workbook