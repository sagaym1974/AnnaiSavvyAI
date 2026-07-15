import {
    ResponsiveContainer,
    ScatterChart,
    Scatter,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ZAxis
} from "recharts";

function formatValue(value) {

    if (value === null || value === undefined)
        return "";

    const num = Number(value);

    if (isNaN(num))
        return value;

    if (Math.abs(num) >= 1000000000)
        return (num / 1000000000).toFixed(2) + "B";

    if (Math.abs(num) >= 1000000)
        return (num / 1000000).toFixed(2) + "M";

    if (Math.abs(num) >= 1000)
        return (num / 1000).toFixed(1) + "K";

    return num.toLocaleString();

}

function CustomTooltip({ active, payload }) {

    if (active && payload && payload.length) {

        const point = payload[0].payload;

        return (

            <div
                style={{
                    background:"#ffffff",
                    border:"1px solid #d9d9d9",
                    borderRadius:"8px",
                    padding:"10px",
                    boxShadow:"0 3px 10px rgba(0,0,0,.15)"
                }}
            >

                <strong>

                    Data Point

                </strong>

                <br/>

                X :

                <b>

                    {" "}

                    {formatValue(payload[0].payload[payload[0].dataKey])}

                </b>

            </div>

        );

    }

    return null;

}

function ScatterChartRenderer({ chart }) {

    if (!chart.data || chart.data.length === 0) {

        return (

            <div
                style={{
                    height:340,
                    display:"flex",
                    alignItems:"center",
                    justifyContent:"center"
                }}
            >

                No Scatter Data

            </div>

        );

    }

    return (

        <ResponsiveContainer
            width="100%"
            height={340}
        >

            <ScatterChart
                margin={{
                    top:20,
                    right:20,
                    left:20,
                    bottom:20
                }}
            >

                <CartesianGrid strokeDasharray="3 3"/>

                <XAxis
                    type="number"
                    dataKey={chart.x_axis}
                    name={chart.x_axis}
                />

                <YAxis
                    type="number"
                    dataKey={chart.y_axis}
                    name={chart.y_axis}
                />

                <ZAxis range={[70,70]}/>

                <Tooltip/>

                <Legend/>

                <Scatter
                    name={chart.business_metric}
                    data={chart.data}
                    fill="#E53935"
                />

            </ScatterChart>

        </ResponsiveContainer>

    );

}

export default ScatterChartRenderer;