import {
    ResponsiveContainer,
    BarChart,
    Bar,
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

function HorizontalBarChartRenderer({ chart }) {

    return (

        <ResponsiveContainer
            width="100%"
            height={340}
        >

            <BarChart

                layout="vertical"

                data={chart.data}

                margin={{
                    top:20,
                    right:30,
                    left:40,
                    bottom:20
                }}

            >

                <CartesianGrid strokeDasharray="3 3"/>

                <XAxis

                    type="number"

                    tickFormatter={formatValue}

                    tick={{
                        fontSize:11
                    }}

                />

                <YAxis

                    type="category"

                    dataKey={chart.y_axis}

                    width={120}

                    tick={{
                        fontSize:11
                    }}

                />

                <Tooltip

                    content={<CustomTooltip/>}

                />

                <Legend/>

                <Bar

                    dataKey={chart.x_axis}

                    fill="#FB8C00"

                    radius={[0,8,8,0]}

                >

                    <LabelList

                        dataKey={chart.x_axis}

                        position="right"

                        formatter={formatValue}

                        style={{
                            fontSize:11,
                            fill:"#222",
                            fontWeight:"bold"
                        }}

                    />

                </Bar>

            </BarChart>

        </ResponsiveContainer>

    );

}

export default HorizontalBarChartRenderer;