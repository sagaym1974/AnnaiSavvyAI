class KPIEngine:

    def generate(self, workbook):

        kpis = []

        domain = workbook.get(
            "domain",
            {}
        ).get(
            "name",
            "General"
        )

        business_health = workbook.get(
            "business_health",
            {}
        )

        # --------------------------------------------------
        # Executive KPIs
        # --------------------------------------------------

        kpis.append({

            "sheet": "Executive",

            "title": "Business Health",

            "subtitle": "Overall",

            "icon": "🟢",

            "priority": 0,

            "value": business_health.get(
                "health_score",
                0
            ),

            "column": "health_score",

            "business_name": "Business Health"

        })

        kpis.append({

            "sheet": "Executive",

            "title": "AI Confidence",

            "subtitle": "Confidence",

            "icon": "🤖",

            "priority": 0,

            "value": business_health.get(
                "confidence_score",
                0
            ),

            "column": "confidence_score",

            "business_name": "AI Confidence"

        })

        # --------------------------------------------------
        # Worksheet KPIs
        # --------------------------------------------------

        for sheet in workbook.get(

            "worksheets",

            []

        ):

            meanings = sheet.get(

                "business_meaning",

                {}

            )

            for column, info in meanings.items():

                if info.get(

                    "business_category"

                ) != "Measure":

                    continue

                stats = info.get(

                    "statistics",

                    {}

                )

                display = info.get(

                    "display_name",

                    column

                )

                metric = info.get(

                    "business_name",

                    column

                )

                base = display.replace(

                    "Total ",

                    ""

                )

                kpis.append({

                    "sheet": sheet["sheet_name"],

                    "title": display,

                    "subtitle": "Total",

                    "icon": "💰",

                    "priority": 1,

                    "value": round(

                        stats.get(

                            "sum",

                            0

                        ),

                        2

                    ),

                    "column": column,

                    "business_name": metric

                })

                kpis.append({

                    "sheet": sheet["sheet_name"],

                    "title": f"Average {base}",

                    "subtitle": "Average",

                    "icon": "📊",

                    "priority": 2,

                    "value": round(

                        stats.get(

                            "average",

                            0

                        ),

                        2

                    ),

                    "column": column,

                    "business_name": metric

                })

                kpis.append({

                    "sheet": sheet["sheet_name"],

                    "title": f"Highest {base}",

                    "subtitle": "Maximum",

                    "icon": "📈",

                    "priority": 3,

                    "value": round(

                        stats.get(

                            "maximum",

                            0

                        ),

                        2

                    ),

                    "column": column,

                    "business_name": metric

                })

                kpis.append({

                    "sheet": sheet["sheet_name"],

                    "title": f"Lowest {base}",

                    "subtitle": "Minimum",

                    "icon": "📉",

                    "priority": 4,

                    "value": round(

                        stats.get(

                            "minimum",

                            0

                        ),

                        2

                    ),

                    "column": column,

                    "business_name": metric

                })

                kpis.append({

                    "sheet": sheet["sheet_name"],

                    "title": f"Median {base}",

                    "subtitle": "Median",

                    "icon": "📌",

                    "priority": 5,

                    "value": round(

                        stats.get(

                            "median",

                            0

                        ),

                        2

                    ),

                    "column": column,

                    "business_name": metric

                })

                kpis.append({

                    "sheet": sheet["sheet_name"],

                    "title": f"Records",

                    "subtitle": metric,

                    "icon": "📋",

                    "priority": 6,

                    "value": stats.get(

                        "count",

                        0

                    ),

                    "column": column,

                    "business_name": metric

                })

        # --------------------------------------------------
        # Domain KPI
        # --------------------------------------------------

        kpis.append({

            "sheet": "Executive",

            "title": "Business Domain",

            "subtitle": domain,

            "icon": "🏢",

            "priority": 99,

            "value": domain,

            "column": "domain",

            "business_name": domain

        })

        workbook["kpis"] = sorted(

            kpis,

            key=lambda x: (

                x["priority"],

                str(x["title"])

            )

        )

        return workbook