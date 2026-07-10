class WorkbookModel:

    def __init__(self, filename):

        self.data = {
            "filename": filename,
            "worksheets": [],
            "relationships": [],
            "kpis": [],
            "charts": [],
            "insights": [],
            "dashboard": {}
        }

    def add_sheet(self, sheet):
        self.data["worksheets"].append(sheet)

    def add_relationship(self, relationship):
        self.data["relationships"].append(relationship)

    def add_kpi(self, kpi):
        self.data["kpis"].append(kpi)

    def add_chart(self, chart):
        self.data["charts"].append(chart)

    def add_insight(self, insight):
        self.data["insights"].append(insight)

    def build(self):
        return self.data