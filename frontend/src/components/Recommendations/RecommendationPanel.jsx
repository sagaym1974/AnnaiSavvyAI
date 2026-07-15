import "../../styles/recommendation.css";

function RecommendationPanel({ dashboardData }) {

    if (!dashboardData) return null;

    const executive =
        dashboardData.executive_intelligence || {};

    const recommendations =
        executive.top_recommendations || [];

    return (

        <section>

            <h2 className="recommendation-heading">

                🤖 AI Recommendations

            </h2>

            <div className="recommendation-grid">

                {

                    recommendations.length === 0 ? (

                        <div className="recommendation-card">

                            <h3>

                                No AI recommendations available

                            </h3>

                        </div>

                    ) : (

                        recommendations.map((item, index) => (

                            <div
                                key={index}
                                className="recommendation-card"
                            >

                                <div
                                    className="recommendation-top"
                                >

                                    <h3>

                                        {item.title}

                                    </h3>

                                    <span
                                        className="priority-badge"
                                    >

                                        {item.priority || "Normal"}

                                    </span>

                                </div>

                                <div
                                    className="recommendation-category"
                                >

                                    {item.category}

                                </div>

                                <p>

                                    {item.message}

                                </p>

                            </div>

                        ))

                    )

                }

            </div>

        </section>

    );

}

export default RecommendationPanel;