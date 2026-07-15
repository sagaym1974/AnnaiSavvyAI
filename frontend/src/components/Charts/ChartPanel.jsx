import "../../styles/charts.css";

import ChartFactory from "./ChartFactory";

function ChartPanel({ dashboardData }) {

    if (!dashboardData) return null;

    const executive =
        dashboardData.executive_intelligence;

    if (!executive) return null;

    const charts =
        executive.top_charts || [];

    return (

        <section id="chart-section">

            <h2 className="chart-heading">

                📈 Executive Charts

            </h2>

            {

                charts.length === 0 && (

                    <div className="chart-empty">

                        No charts generated.

                    </div>

                )

            }

            <div className="chart-grid">

                {

                    charts.map((chart, index) => (

                        <div
                            key={index}
                            className="chart-card"
                        >

                            <div className="chart-title">

                                {chart.title}

                            </div>

                            <div className="chart-subtitle">

                                <strong>

                                    {chart.domain || "General"}

                                </strong>

                                {

                                    chart.business_metric &&

                                    <> • {chart.business_metric}</>

                                }

                            </div>

                            <ChartFactory
                                chart={chart}
                            />

                        </div>

                    ))

                }

            </div>

        </section>

    );

}

export default ChartPanel;