import "../../styles/kpi.css";

function KPICards({ dashboardData }) {

    if (!dashboardData) return null;

    const executive =
        dashboardData.executive_intelligence;

    if (!executive) return null;

    const kpis =
        executive.top_kpis || [];

    return (

        <section id="kpi-section">

            <h2 className="kpi-heading">

                ⭐ Executive KPIs

            </h2>

            <div className="kpi-grid">

                {

                    kpis.length === 0 ? (

                        <div
                            className="kpi-card"
                        >

                            <div
                                className="kpi-title"
                            >

                                No KPIs Generated

                            </div>

                        </div>

                    ) : (

                        kpis.map((kpi, index) => (

                            <div
                                key={index}
                                className="kpi-card"
                            >

                                <div className="kpi-top">

                                    <div
                                        className="kpi-icon"
                                    >

                                        {kpi.icon || "📊"}

                                    </div>

                                    <div
                                        className="kpi-sheet"
                                    >

                                        {kpi.sheet}

                                    </div>

                                </div>

                                <div
                                    className="kpi-title"
                                >

                                    {kpi.title}

                                </div>

                                <div
                                    className="kpi-subtitle"
                                >

                                    {kpi.subtitle || ""}

                                </div>

                                <div
                                    className="kpi-value"
                                >

                                    {

                                        typeof kpi.value === "number"

                                            ?

                                            Number(

                                                kpi.value

                                            ).toLocaleString(

                                                undefined,

                                                {

                                                    minimumFractionDigits: 0,

                                                    maximumFractionDigits: 2

                                                }

                                            )

                                            :

                                            kpi.value

                                    }

                                </div>

                                <div
                                    className="kpi-footer"
                                >

                                    {

                                        kpi.business_name ||

                                        ""

                                    }

                                </div>

                            </div>

                        ))

                    )

                }

            </div>

        </section>

    );

}

export default KPICards;