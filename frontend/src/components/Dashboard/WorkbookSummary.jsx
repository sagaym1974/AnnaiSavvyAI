function WorkbookSummary({ dashboardData }) {

    if (!dashboardData) return null;

    const worksheets = dashboardData.worksheets || [];

    const workbookContext =
        dashboardData.workbook_context || {};

    const domain =
        dashboardData.domain || {};

    return (

        <section
            id="report-section"
            style={{
                marginTop: "30px",
                marginBottom: "30px"
            }}
        >

            <h2
                style={{
                    color: "#0B5394",
                    marginBottom: "20px"
                }}
            >

                📁 Workbook Explorer

            </h2>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
                    gap: "15px",
                    marginBottom: "25px"
                }}
            >

                <div
                    style={{
                        background: "#ffffff",
                        padding: "18px",
                        borderRadius: "10px",
                        boxShadow: "0 2px 8px rgba(0,0,0,.08)"
                    }}
                >

                    <h4>Business Domain</h4>

                    <h2
                        style={{
                            color: "#0B5394"
                        }}
                    >

                        {domain.name || "General"}

                    </h2>

                </div>

                <div
                    style={{
                        background: "#ffffff",
                        padding: "18px",
                        borderRadius: "10px",
                        boxShadow: "0 2px 8px rgba(0,0,0,.08)"
                    }}
                >

                    <h4>Worksheets</h4>

                    <h2
                        style={{
                            color: "#0B5394"
                        }}
                    >

                        {workbookContext.worksheet_count ?? worksheets.length}

                    </h2>

                </div>

                <div
                    style={{
                        background: "#ffffff",
                        padding: "18px",
                        borderRadius: "10px",
                        boxShadow: "0 2px 8px rgba(0,0,0,.08)"
                    }}
                >

                    <h4>Total Columns</h4>

                    <h2
                        style={{
                            color: "#0B5394"
                        }}
                    >

                        {workbookContext.column_count ?? 0}

                    </h2>

                </div>

                <div
                    style={{
                        background: "#ffffff",
                        padding: "18px",
                        borderRadius: "10px",
                        boxShadow: "0 2px 8px rgba(0,0,0,.08)"
                    }}
                >

                    <h4>Total Rows</h4>

                    <h2
                        style={{
                            color: "#0B5394"
                        }}
                    >

                        {workbookContext.row_count ?? 0}

                    </h2>

                </div>

            </div>

            <table
                style={{
                    width: "100%",
                    borderCollapse: "collapse",
                    background: "white",
                    boxShadow: "0 2px 8px rgba(0,0,0,.08)"
                }}
            >

                <thead>

                    <tr
                        style={{
                            background: "#0B5394",
                            color: "white"
                        }}
                    >

                        <th style={{ padding: "12px" }}>

                            Worksheet

                        </th>

                        <th style={{ padding: "12px" }}>

                            Dataset Type

                        </th>

                        <th style={{ padding: "12px" }}>

                            Rows

                        </th>

                        <th style={{ padding: "12px" }}>

                            Columns

                        </th>

                        <th style={{ padding: "12px" }}>

                            Numeric Columns

                        </th>

                        <th style={{ padding: "12px" }}>

                            Date Columns

                        </th>

                    </tr>

                </thead>

                <tbody>

                    {

                        worksheets.map((sheet, index) => (

                            <tr
                                key={index}
                                style={{
                                    borderBottom: "1px solid #e5e5e5"
                                }}
                            >

                                <td style={{ padding: "12px" }}>

                                    {sheet.sheet_name}

                                </td>

                                <td style={{ padding: "12px" }}>

                                    {sheet.dataset_type}

                                </td>

                                <td style={{ padding: "12px" }}>

                                    {sheet.rows}

                                </td>

                                <td style={{ padding: "12px" }}>

                                    {sheet.columns}

                                </td>

                                <td style={{ padding: "12px" }}>

                                    {(sheet.numeric_columns || []).join(", ")}

                                </td>

                                <td style={{ padding: "12px" }}>

                                    {(sheet.date_columns || []).join(", ")}

                                </td>

                            </tr>

                        ))

                    }

                </tbody>

            </table>

        </section>

    );

}

export default WorkbookSummary;