from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router

app = FastAPI(

    title="Annai Savvy AI",

    description="AI Powered Business Intelligence Platform",

    version="1.0.0"

)

# -------------------------------------------------------
# CORS
# -------------------------------------------------------

origins = [

    # Local Development

    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://localhost:5176",

    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://127.0.0.1:5175",
    "http://127.0.0.1:5176",

    # Production (Vercel)

    "https://annai-savvy-2mhfz3f07-annaisavvyai.vercel.app",

    # Optional - Future Vercel Domain

    "https://annai-savvy-ai.vercel.app"

]

app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)

# -------------------------------------------------------
# API Routes
# -------------------------------------------------------

app.include_router(

    upload_router,

    prefix="/api",

    tags=["Workbook Analysis"]

)

# -------------------------------------------------------
# Home
# -------------------------------------------------------

@app.get("/")

def home():

    return {

        "application": "Annai Savvy AI",

        "version": "1.0.0",

        "status": "Running",

        "message": "Welcome to Annai Savvy AI Business Intelligence Platform.",

        "available_endpoints": {

            "upload": "/api/upload",

            "swagger": "/docs",

            "redoc": "/redoc"

        }

    }

# -------------------------------------------------------
# Health Check
# -------------------------------------------------------

@app.get("/health")

def health():

    return {

        "status": "Healthy",

        "application": "Annai Savvy AI",

        "backend": "FastAPI",

        "version": "1.0.0"

    }

# -------------------------------------------------------
# AI Information
# -------------------------------------------------------

@app.get("/about")

def about():

    return {

        "name": "Annai Savvy AI",

        "category": "AI Business Intelligence",

        "features": [

            "Workbook Analysis",

            "Executive Dashboard",

            "AI Recommendations",

            "Business Health Score",

            "Interactive KPIs",

            "Charts",

            "Insights",

            "Executive Intelligence"

        ]

    }