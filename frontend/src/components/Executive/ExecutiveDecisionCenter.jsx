import "../../styles/executive.css";

function ExecutiveDecisionCenter({ dashboardData }) {

    if (!dashboardData) return null;

    const executive =
        dashboardData.executive_intelligence || {};

    const health =
        executive.business_health || {};

    const confidence =
        executive.confidence || {};

    const forecast =
        executive.forecast_readiness || {};

    const domain =
        executive.domain || {};

    return (

        <section className="decision-center">

            <h2 className="decision-heading">

                🧠 Executive Decision Center

            </h2>

            <div className="decision-grid">

                <div className="decision-card compact">

                    <div className="decision-title">

                        Domain

                    </div>

                    <div className="decision-value">

                        {domain.name || "General"}

                    </div>

                </div>

                <div className="decision-card compact">

                    <div className="decision-title">

                        Health

                    </div>

                    <div className="decision-value">

                        {health.health_score ?? 0}%

                    </div>

                </div>

                <div className="decision-card compact">

                    <div className="decision-title">

                        Forecast

                    </div>

                    <div className="decision-value">

                        {forecast.status || "Ready"}

                    </div>

                </div>

                <div className="decision-card compact">

                    <div className="decision-title">

                        Confidence

                    </div>

                    <div className="decision-value">

                        {confidence.score ?? 0}%

                    </div>

                </div>

            </div>

        </section>

    );

}

export default ExecutiveDecisionCenter;