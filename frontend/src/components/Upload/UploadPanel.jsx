import { useRef, useState } from "react";
import api from "../../services/api";
import "../../styles/upload.css";

function UploadPanel({ dashboardData, setDashboardData }) {

    const fileInput = useRef(null);

    const [selectedFile, setSelectedFile] = useState(null);
    const [fileName, setFileName] = useState("No workbook selected");

    const executive =
        dashboardData?.executive_intelligence || {};

    const businessHealth =
        executive.business_health || {};

    const quality =
        executive.data_quality || {};

    const forecast =
        executive.forecast_readiness || {};

    const confidence =
        executive.confidence || {};

    const uploadFile = async () => {

        if (!selectedFile) {

            alert("Please select an Excel workbook.");

            return;

        }

        const formData = new FormData();

        formData.append("file", selectedFile);

        try {

            const response = await api.post(

                "/upload",

                formData,

                {

                    headers: {

                        "Content-Type":
                            "multipart/form-data"

                    }

                }

            );

            console.clear();

            console.log("======================================");
            console.log("FULL RESPONSE");
            console.log(response.data);

            console.log("======================================");
            console.log("TOP CHARTS");
            console.log(
                response.data.executive_intelligence?.top_charts
            );

            console.log("======================================");
            console.log("FIRST CHART");
            console.log(
                response.data.executive_intelligence?.top_charts?.[0]
            );

            console.log("======================================");

            setDashboardData(response.data);

        }

        catch (error) {

            console.log(error);

            alert("Upload Failed");

        }

    };

    return (

        <section className="upload-ribbon">

            <div className="upload-left">

                <div className="upload-title">

                    📁 Upload Workbook

                </div>

                <input

                    ref={fileInput}

                    hidden

                    type="file"

                    accept=".xlsx,.xls,.csv"

                    onChange={(e)=>{

                        const file=e.target.files[0];

                        setSelectedFile(file);

                        setFileName(

                            file

                            ? file.name

                            : "No workbook selected"

                        );

                    }}

                />

                <button

                    type="button"

                    className="browse-button"

                    onClick={()=>fileInput.current.click()}

                >

                    Browse

                </button>

                <div className="upload-file">

                    {fileName}

                </div>

                <button

                    type="button"

                    className="upload-button"

                    onClick={uploadFile}

                >

                    Analyze Workbook

                </button>

            </div>

            <div className="upload-right">

                <div className="alert-title">

                    🚨 AI Alert Center

                </div>

                <div className="alert-chip success">

                    <strong>Status</strong>

                    {

                        dashboardData

                        ? "Healthy"

                        : "Waiting"

                    }

                </div>

                <div className="alert-chip">

                    <strong>Health</strong>

                    {businessHealth.health_score ?? "--"}%

                </div>

                <div className="alert-chip">

                    <strong>Quality</strong>

                    {quality.score ?? "--"}%

                </div>

                <div className="alert-chip">

                    <strong>Forecast</strong>

                    {forecast.status ?? "--"}

                </div>

                <div className="alert-chip">

                    <strong>Confidence</strong>

                    {confidence.score ?? "--"}%

                </div>

            </div>

        </section>

    );

}

export default UploadPanel;