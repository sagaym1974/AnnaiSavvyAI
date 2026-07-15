import BarChartRenderer from "./Renderers/BarChartRenderer";
import LineChartRenderer from "./Renderers/LineChartRenderer";
import PieChartRenderer from "./Renderers/PieChartRenderer";
import ScatterChartRenderer from "./Renderers/ScatterChartRenderer";
import AreaChartRenderer from "./Renderers/AreaChartRenderer";
import HorizontalBarChartRenderer from "./Renderers/HorizontalBarChartRenderer";

function ChartFactory({ chart }) {

    switch (chart.chart_type) {

        case "bar":

            return (

                <BarChartRenderer

                    chart={chart}

                />

            );

        case "line":

            return (

                <LineChartRenderer

                    chart={chart}

                />

            );

        case "pie":

            return (

                <PieChartRenderer

                    chart={chart}

                />

            );

        case "scatter":

            return (

                <ScatterChartRenderer

                    chart={chart}

                />

            );

        case "area":

            return (

                <AreaChartRenderer

                    chart={chart}

                />

            );

        case "horizontal_bar":

            return (

                <HorizontalBarChartRenderer

                    chart={chart}

                />

            );

        default:

            return (

                <div
                    style={{
                        height: 340,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: "#888",
                        fontWeight: 600
                    }}
                >

                    Unsupported Chart Type :
                    {" "}
                    {chart.chart_type}

                </div>

            );

    }

}

export default ChartFactory;