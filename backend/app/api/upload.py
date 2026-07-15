from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.excel_reader import read_excel_workbook
from app.services.dataset_analyzer import DatasetAnalyzer
from app.services.ai_recommendation_engine import AIRecommendationEngine

router = APIRouter()

analyzer = DatasetAnalyzer()

recommendation_engine = AIRecommendationEngine()


@router.post("/upload")
async def upload_excel(file: UploadFile = File(...)):

    # ----------------------------------------------------
    # Validate Upload
    # ----------------------------------------------------

    if not file.filename:

        raise HTTPException(

            status_code=400,

            detail="No file selected."

        )

    if not (

        file.filename.endswith(".xlsx")

        or

        file.filename.endswith(".xls")

        or

        file.filename.endswith(".csv")

    ):

        raise HTTPException(

            status_code=400,

            detail="Only Excel (.xlsx, .xls) and CSV files are supported."

        )

    try:

        # ----------------------------------------------------
        # Read Workbook
        # ----------------------------------------------------

        workbook = read_excel_workbook(

            file.file,

            file.filename

        )

        # ----------------------------------------------------
        # Core Analysis
        # ----------------------------------------------------

        workbook = analyzer.analyze(

            workbook

        )

        # ----------------------------------------------------
        # AI Executive Recommendations
        # ----------------------------------------------------

        executive = workbook.get(

            "executive_intelligence",

            {}

        )

        executive_recommendations = recommendation_engine.generate(

            executive

        )

        executive["top_recommendations"] = executive_recommendations

        workbook["executive_intelligence"] = executive

        # ----------------------------------------------------
        # Response Metadata
        # ----------------------------------------------------

        workbook["analysis"] = {

            "status": "Success",

            "engine": "Annai Savvy AI v1.0",

            "uploaded_file": file.filename,

            "worksheets": len(

                workbook.get(

                    "worksheets",

                    []

                )

            ),

            "kpis": len(

                workbook.get(

                    "kpis",

                    []

                )

            ),

            "charts": len(

                workbook.get(

                    "charts",

                    []

                )

            ),

            "insights": sum(

                len(

                    sheet.get(

                        "items",

                        []

                    )

                )

                for sheet in workbook.get(

                    "insights",

                    []

                )

            ),

            "recommendations": len(

                executive_recommendations

            )

        }

        return workbook

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=f"Analysis failed: {str(e)}"

        )