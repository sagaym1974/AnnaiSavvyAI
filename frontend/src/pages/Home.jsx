import { useState } from "react";

import Header from "../components/Common/Header";
import Sidebar from "../components/Common/Sidebar";
import Footer from "../components/Common/Footer";

import UploadPanel from "../components/Upload/UploadPanel";
import AlertPanel from "../components/Alerts/AlertPanel";

import ExecutiveDashboard from "../components/Dashboard/ExecutiveDashboard";

import SettingsPanel from "../components/Common/SettingsPanel";

import "../styles/upload.css";

function Home() {

    const [dashboardData, setDashboardData] = useState(null);

    return (

        <div className="app-layout">

            <Sidebar />

            <div className="main-content">

                <Header />

                <div className="top-dashboard-row">

                    <div className="top-upload-panel">

                        <UploadPanel
    dashboardData={dashboardData}
    setDashboardData={setDashboardData}
/>

                    </div>

                    

                </div>

                {

                    dashboardData &&

                    (

                        <>

                            <ExecutiveDashboard

                                dashboardData={dashboardData}

                            />

                            <SettingsPanel />

                        </>

                    )

                }

                <Footer />

            </div>

        </div>

    );

}

export default Home;