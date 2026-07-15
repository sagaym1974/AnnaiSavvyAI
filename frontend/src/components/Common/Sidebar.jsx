import "../../styles/common.css";
import logo from "../../assets/logo.png";

function Sidebar() {

    const scrollToSection = (id) => {

        const section = document.getElementById(id);

        if (section) {

            section.scrollIntoView({

                behavior: "smooth",

                block: "start"

            });

        }

    };

    return (

        <aside className="sidebar">

            <div className="sidebar-logo">

                <img

                    src={logo}

                    alt="Annai Savvy AI"

                    className="sidebar-logo-image"

                />

                <h2>

                    Annai Savvy AI

                </h2>

                <div
                    style={{
                        fontSize: "11px",
                        opacity: ".8",
                        marginTop: "3px"
                    }}
                >

                    Enterprise BI

                </div>

            </div>

            <hr
                style={{
                    opacity: ".25",
                    marginBottom: "18px"
                }}
            />

            <nav>

                <button

                    className="menu-button"

                    onClick={() => scrollToSection("upload-section")}

                >

                    📁 Upload Workbook

                </button>

                <button

                    className="menu-button"

                    onClick={() => scrollToSection("kpi-section")}

                >

                    📊 KPI Dashboard

                </button>

                <button

                    className="menu-button"

                    onClick={() => scrollToSection("chart-section")}

                >

                    📈 Charts

                </button>

                <button

                    className="menu-button"

                    onClick={() => scrollToSection("insight-section")}

                >

                    🧠 Executive Intelligence

                </button>

                <button

                    className="menu-button"

                    onClick={() => scrollToSection("report-section")}

                >

                    📄 Workbook Explorer

                </button>

                <button

                    className="menu-button"

                    onClick={() => scrollToSection("settings-section")}

                >

                    ⚙ Settings

                </button>

            </nav>

            <div
                style={{
                    position: "absolute",
                    bottom: "20px",
                    left: "15px",
                    right: "15px",
                    fontSize: "11px",
                    textAlign: "center",
                    opacity: ".70"
                }}
            >

                Version 1.0

                <br />

                © Annai Savvy Associates

            </div>

        </aside>

    );

}

export default Sidebar;