import "../../styles/charts.css";

import ChartFactory from "./ChartFactory";

function ChartPanel({ dashboardData }) {

    if (!dashboardData) {

        return null;

    }

    if (!dashboardData.charts) {

        return null;

    }

    const charts = [...dashboardData.charts].sort(

        (a, b) => (a.priority || 999) - (b.priority || 999)

    );

    return (

        <section>

            <h2 className="chart-heading">

                📊 Executive Visual Analytics

            </h2>

            <div className="chart-grid">

                {

                    charts.map((chart, index) => (

                        <ChartFactory

                            key={index}

                            chart={chart}

                        />

                    ))

                }

            </div>

        </section>

    );

}

export default ChartPanel;