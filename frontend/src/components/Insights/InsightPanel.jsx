import "../../styles/insights.css";

function InsightPanel({ dashboardData }) {

    if (!dashboardData) return null;

    const executive =
        dashboardData.executive_intelligence;

    if (!executive) return null;

    const insights =
        executive.top_insights || [];

    return (

        <section id="insight-section">

            <h2 className="insight-heading">

                🧠 Executive Intelligence

            </h2>

            {

                insights.length === 0 ? (

                    <div className="insight-sheet">

                        <div className="insight-card info">

                            <div className="insight-icon">

                                ℹ️

                            </div>

                            <div className="insight-content">

                                <h4>

                                    No Executive Insights

                                </h4>

                                <p>

                                    AI could not generate executive insights
                                    for this workbook.

                                </p>

                            </div>

                        </div>

                    </div>

                ) : (

                    <div className="insight-sheet">

                        {

                            insights.map((item, index) => (

                                <div

                                    key={index}

                                    className={`insight-card ${item.severity || "info"}`}

                                >

                                    <div className="insight-icon">

                                        {item.icon || "💡"}

                                    </div>

                                    <div className="insight-content">

                                        <h4>

                                            {item.title}

                                        </h4>

                                        <small>

                                            {item.category}

                                        </small>

                                        <p>

                                            {item.message}

                                        </p>

                                    </div>

                                </div>

                            ))

                        }

                    </div>

                )

            }

        </section>

    );

}

export default InsightPanel;