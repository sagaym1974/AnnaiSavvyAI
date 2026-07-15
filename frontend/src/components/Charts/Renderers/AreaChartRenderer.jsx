import {
    ResponsiveContainer,
    AreaChart,
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    LabelList
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

function CustomTooltip({ active, payload, label }) {

    if (active && payload && payload.length) {

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

                    {label}

                </strong>

                <br/>

                {payload[0].name}

                <b>

                    {" "}

                    {formatValue(payload[0].value)}

                </b>

            </div>

        );

    }

    return null;

}

function AreaChartRenderer({ chart }) {

    return (

        <ResponsiveContainer
            width="100%"
            height={340}
        >

            <AreaChart

                data={chart.data}

                margin={{
                    top:20,
                    right:20,
                    left:10,
                    bottom:20
                }}

            >

                <CartesianGrid strokeDasharray="3 3"/>

                <XAxis

                    dataKey={chart.x_axis}

                    tick={{
                        fontSize:11
                    }}

                />

                <YAxis

                    tickFormatter={formatValue}

                    tick={{
                        fontSize:11
                    }}

                />

                <Tooltip

                    content={<CustomTooltip/>}

                />

                <Legend/>

                <Area

                    type="monotone"

                    dataKey={chart.y_axis}

                    stroke="#1976D2"

                    fill="#90CAF9"

                    strokeWidth={3}

                >

                    <LabelList

                        dataKey={chart.y_axis}

                        position="top"

                        formatter={formatValue}

                        style={{
                            fontSize:11,
                            fill:"#222",
                            fontWeight:"bold"
                        }}

                    />

                </Area>

            </AreaChart>

        </ResponsiveContainer>

    );

}

export default AreaChartRenderer;