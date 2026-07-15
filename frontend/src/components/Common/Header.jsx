import "../../styles/common.css";
import logo from "../../assets/logo.png";

function Header() {

    return (

        <header className="header">

            <div className="header-container">

                <div className="header-left">

                    <img
                        src={logo}
                        alt="Annai Savvy AI"
                        className="header-logo"
                    />

                    <div>

                        <h1>

                            Annai Savvy AI

                        </h1>

                        <p>

                            Intelligent Business Intelligence Platform

                        </p>

                    </div>

                </div>

                <div className="header-right">

                    <div className="status-chip">

                        🟢 AI Ready

                    </div>

                    <div className="status-chip">

                        📊 Executive Dashboard

                    </div>

                </div>

            </div>

        </header>

    );

}

export default Header;