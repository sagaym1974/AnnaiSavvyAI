import ExecutiveDecisionCenter from "../Executive/ExecutiveDecisionCenter";

import KPICards from "../KPI/KPICards";

import ChartPanel from "../Charts/ChartPanel";

import RecommendationPanel from "../Recommendations/RecommendationPanel";

import InsightPanel from "../Insights/InsightPanel";

import WorkbookSummary from "./WorkbookSummary";

import ExecutiveSummary from "../Executive/ExecutiveSummary";

function ExecutiveDashboard({ dashboardData }) {

    if (!dashboardData) return null;

    return (

        <>

            <ExecutiveSummary

                dashboardData={dashboardData}

            />

            <ExecutiveDecisionCenter

                dashboardData={dashboardData}

            />

            <KPICards

                dashboardData={dashboardData}

            />

            <ChartPanel

                dashboardData={dashboardData}

            />

            <RecommendationPanel

                dashboardData={dashboardData}

            />

            <InsightPanel

                dashboardData={dashboardData}

            />

            <WorkbookSummary

                dashboardData={dashboardData}

            />

        </>

    );

}

export default ExecutiveDashboard;