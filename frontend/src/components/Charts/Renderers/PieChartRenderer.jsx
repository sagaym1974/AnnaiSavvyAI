import {
    ResponsiveContainer,
    PieChart,
    Pie,
    Cell,
    Tooltip,
    Legend
} from "recharts";

const COLORS = [
    "#1565C0",
    "#43A047",
    "#FB8C00",
    "#E53935",
    "#8E24AA",
    "#00ACC1",
    "#6D4C41",
    "#3949AB",
    "#26A69A",
    "#F4511E"
];

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

function renderLabel({

    name,

    percent,

    value

}) {

    return `${name} ${(percent * 100).toFixed(1)}%`;

}

function CustomTooltip({

    active,

    payload

}) {

    if (

        active &&

        payload &&

        payload.length

    ) {

        const item = payload[0];

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

                    {item.name}

                </strong>

                <br/>

                Value

                <b>

                    {" "}

                    {formatValue(item.value)}

                </b>

            </div>

        );

    }

    return null;

}

function PieChartRenderer({ chart }) {

    return (

        <ResponsiveContainer

            width="100%"

            height={360}

        >

            <PieChart>

                <Pie

                    data={chart.data}

                    dataKey={chart.value}

                    nameKey={chart.label}

                    cx="50%"

                    cy="50%"

                    innerRadius={45}

                    outerRadius={120}

                    paddingAngle={2}

                    label={renderLabel}

                >

                    {

                        chart.data.map((entry,index)=>(

                            <Cell

                                key={index}

                                fill={

                                    COLORS[

                                        index %

                                        COLORS.length

                                    ]

                                }

                            />

                        ))

                    }

                </Pie>

                <Tooltip

                    content={<CustomTooltip/>}

                />

                <Legend

                    verticalAlign="bottom"

                    height={40}

                />

            </PieChart>

        </ResponsiveContainer>

    );

}

export default PieChartRenderer;