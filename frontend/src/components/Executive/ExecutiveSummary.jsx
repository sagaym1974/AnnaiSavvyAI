import "../../styles/insights.css";

function ExecutiveSummary({ dashboardData }) {

    if (!dashboardData) return null;

    const workbook =
        dashboardData.workbook_context || {};

    const domain =
        dashboardData.domain || {};

    const executive =
        dashboardData.executive_intelligence || {};

    const quality =
        executive.data_quality || {};

    const forecast =
        executive.forecast_readiness || {};

    return (

        <section
            className="summary-card"
            style={{
                marginBottom: "18px"
            }}
        >

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    flexWrap: "wrap",
                    gap: "15px"
                }}
            >

                <div
                    style={{
                        flex: 2,
                        minWidth: "350px"
                    }}
                >

                    <h2
                        style={{
                            marginBottom: "8px"
                        }}
                    >

                        🤖 AI Executive Summary

                    </h2>

                    <p
                        style={{
                            margin: 0,
                            color: "#555",
                            lineHeight: "1.6"
                        }}
                    >

                        {

                            executive.summary ||

                            `The uploaded workbook "${dashboardData.filename}" belongs to the ${domain.name || "General"} business domain. AI successfully analysed the workbook and generated KPIs, charts, recommendations and business insights.`

                        }

                    </p>

                </div>

                <div
                    style={{
                        display: "flex",
                        gap: "10px",
                        flexWrap: "wrap"
                    }}
                >

                    <div className="mini-summary-box">

                        <strong>Domain</strong>

                        <br />

                        {domain.name || "General"}

                    </div>

                    <div className="mini-summary-box">

                        <strong>Sheets</strong>

                        <br />

                        {workbook.worksheet_count ?? dashboardData.worksheets.length}

                    </div>

                    <div className="mini-summary-box">

                        <strong>Forecast</strong>

                        <br />

                        {forecast.status || "Ready"}

                    </div>

                    <div className="mini-summary-box">

                        <strong>Quality</strong>

                        <br />

                        {quality.score ?? 100}%

                    </div>

                    <div className="mini-summary-box">

                        <strong>Missing</strong>

                        <br />

                        {quality.missing ?? 0}

                    </div>

                    <div className="mini-summary-box">

                        <strong>Duplicate</strong>

                        <br />

                        {quality.duplicates ?? 0}

                    </div>

                    <div className="mini-summary-box">

                        <strong>Empty</strong>

                        <br />

                        {quality.empty_columns ?? 0}

                    </div>

                </div>

            </div>

        </section>

    );

}

export default ExecutiveSummary;