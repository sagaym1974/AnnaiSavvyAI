from app.services.dataset_identifier import identify_dataset
from app.services.relationship_detector import RelationshipDetector
from app.services.kpi_engine import KPIEngine
from app.services.chart_engine import ChartEngine
from app.services.dashboard_engine import DashboardEngine


class DatasetAnalyzer:

    def __init__(self):

        self.relationship_detector = RelationshipDetector()
        self.kpi_engine = KPIEngine()
        self.chart_engine = ChartEngine()
        self.dashboard_engine = DashboardEngine()

    def analyze(self, workbook):

        for sheet in workbook["worksheets"]:

            columns = sheet["column_names"]

            sheet["dataset_type"] = identify_dataset(columns)

            sheet["primary_key_candidates"] = self.find_primary_keys(columns)

            sheet["date_columns"] = self.find_date_columns(columns)

            sheet["numeric_columns"] = self.find_numeric_columns(
                sheet["sample_data"]
            )

        workbook = self.relationship_detector.detect(workbook)

        workbook = self.kpi_engine.generate(workbook)

        workbook = self.chart_engine.generate(workbook)

        workbook = self.dashboard_engine.generate(workbook)

        return workbook

    def find_primary_keys(self, columns):

        keywords = [
            "id",
            "code",
            "number",
            "no",
            "key"
        ]

        result = []

        for column in columns:

            lower = column.lower()

            if any(word in lower for word in keywords):
                result.append(column)

        return result

    def find_date_columns(self, columns):

        keywords = [
            "date",
            "month",
            "year",
            "time"
        ]

        result = []

        for column in columns:

            lower = column.lower()

            if any(word in lower for word in keywords):
                result.append(column)

        return result

    def find_numeric_columns(self, sample_data):

        if len(sample_data) == 0:
            return []

        numeric = []

        first_row = sample_data[0]

        for column, value in first_row.items():

            if isinstance(value, (int, float)):
                numeric.append(column)

        return numeric