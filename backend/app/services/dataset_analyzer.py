from app.services.dataset_identifier import identify_dataset

from app.services.relationship_detector import RelationshipDetector
from app.services.statistics_engine import StatisticsEngine
from app.services.semantic_engine import SemanticEngine
from app.services.presentation_intelligence_engine import PresentationIntelligenceEngine

from app.services.workbook_context_engine import WorkbookContextEngine
from app.services.domain_detection_engine import DomainDetectionEngine
from app.services.business_meaning_engine import BusinessMeaningEngine
from app.services.metadata_engine import MetadataEngine
from app.services.column_intelligence_engine import ColumnIntelligenceEngine

from app.services.pattern_engine import PatternEngine
from app.services.data_quality_engine import DataQualityEngine
from app.services.anomaly_engine import AnomalyEngine
from app.services.business_health_engine import BusinessHealthEngine
from app.services.recommendation_engine import RecommendationEngine

from app.services.kpi_engine import KPIEngine
from app.services.chart_engine import ChartEngine
from app.services.insight_engine import InsightEngine

from app.services.executive_intelligence_engine import ExecutiveIntelligenceEngine

# ---------------------------------------------------------
# NEW V2 ENGINES
# ---------------------------------------------------------

from app.services.aggregation_engine import AggregationEngine
from app.services.ranking_engine import RankingEngine
from app.services.trend_engine import TrendEngine
from app.services.correlation_engine import CorrelationEngine
from app.services.forecasting_engine import ForecastingEngine
from app.services.segmentation_engine import SegmentationEngine
from app.services.benchmarking_engine import BenchmarkingEngine
from app.services.scoring_engine import ScoringEngine
from app.services.storytelling_engine import StorytellingEngine
from app.services.prediction_engine import PredictionEngine
from app.services.executive_score_engine import ExecutiveScoreEngine
from app.services.executive_alert_engine import ExecutiveAlertEngine
from app.services.opportunity_engine import OpportunityEngine
from app.services.risk_engine import RiskEngine
from app.services.forecasting_ai_engine import ForecastingAIEngine
from app.services.dashboard_builder_engine import DashboardBuilderEngine
from app.services.narrative_engine import NarrativeEngine
from app.services.ai_summary_engine import AISummaryEngine
from app.services.executive_reporting_engine import ExecutiveReportingEngine


class DatasetAnalyzer:

    def __init__(self):

        # --------------------------------------------------
        # CORE ENGINES
        # --------------------------------------------------

        self.relationship_detector = RelationshipDetector()

        self.statistics_engine = StatisticsEngine()

        self.semantic_engine = SemanticEngine()

        self.presentation_intelligence_engine = PresentationIntelligenceEngine()

        self.workbook_context_engine = WorkbookContextEngine()

        self.domain_detection_engine = DomainDetectionEngine()

        self.business_meaning_engine = BusinessMeaningEngine()

        self.metadata_engine = MetadataEngine()

        self.column_intelligence_engine = ColumnIntelligenceEngine()

        self.pattern_engine = PatternEngine()

        self.data_quality_engine = DataQualityEngine()

        self.anomaly_engine = AnomalyEngine()

        self.business_health_engine = BusinessHealthEngine()

        self.recommendation_engine = RecommendationEngine()

        self.kpi_engine = KPIEngine()

        self.chart_engine = ChartEngine()

        self.insight_engine = InsightEngine()

        self.executive_intelligence_engine = ExecutiveIntelligenceEngine()

        # --------------------------------------------------
        # V2 AI ENGINES
        # --------------------------------------------------

        self.aggregation_engine = AggregationEngine()

        self.ranking_engine = RankingEngine()

        self.trend_engine = TrendEngine()

        self.correlation_engine = CorrelationEngine()

        self.forecasting_engine = ForecastingEngine()

        self.segmentation_engine = SegmentationEngine()

        self.benchmarking_engine = BenchmarkingEngine()

        self.scoring_engine = ScoringEngine()

        self.storytelling_engine = StorytellingEngine()

        self.prediction_engine = PredictionEngine()

        self.executive_score_engine = ExecutiveScoreEngine()

        self.executive_alert_engine = ExecutiveAlertEngine()

        self.opportunity_engine = OpportunityEngine()

        self.risk_engine = RiskEngine()

        self.forecasting_ai_engine = ForecastingAIEngine()

        self.dashboard_builder_engine = DashboardBuilderEngine()

        self.narrative_engine = NarrativeEngine()

        self.ai_summary_engine = AISummaryEngine()

        self.executive_reporting_engine = ExecutiveReportingEngine()

    def analyze(self, workbook):

        # --------------------------------------------------
        # INITIAL ANALYSIS
        # --------------------------------------------------

        for sheet in workbook.get("worksheets", []):

            columns = sheet.get(
                "column_names",
                []
            )

            sheet["dataset_type"] = identify_dataset(columns)

            sheet["primary_key_candidates"] = self.find_primary_keys(columns)

            sheet["date_columns"] = self.find_date_columns(columns)

            sheet["numeric_columns"] = self.find_numeric_columns(

                sheet.get(
                    "sample_data",
                    []
                )

            )

        # --------------------------------------------------
        # CORE PIPELINE
        # --------------------------------------------------

        workbook = self.relationship_detector.detect(workbook)

        workbook = self.statistics_engine.generate(workbook)

        workbook = self.semantic_engine.generate(workbook)

        workbook = self.presentation_intelligence_engine.generate(workbook)

        workbook = self.workbook_context_engine.generate(workbook)

        workbook = self.domain_detection_engine.generate(workbook)

        workbook = self.business_meaning_engine.generate(workbook)

        workbook = self.metadata_engine.generate(workbook)

        workbook = self.column_intelligence_engine.generate(workbook)

        workbook = self.pattern_engine.generate(workbook)

        workbook = self.data_quality_engine.generate(workbook)

        workbook = self.anomaly_engine.generate(workbook)

        workbook = self.business_health_engine.generate(workbook)

        workbook = self.recommendation_engine.generate(workbook)

        workbook = self.kpi_engine.generate(workbook)

        workbook = self.chart_engine.generate(workbook)

        workbook = self.insight_engine.generate(workbook)

        workbook = self.executive_intelligence_engine.generate(workbook)

        # --------------------------------------------------
        # V2 AI PIPELINE
        # --------------------------------------------------

        workbook = self.aggregation_engine.generate(workbook)

        workbook = self.ranking_engine.generate(workbook)

        workbook = self.trend_engine.generate(workbook)

        workbook = self.correlation_engine.generate(workbook)

        workbook = self.forecasting_engine.generate(workbook)

        workbook = self.segmentation_engine.generate(workbook)

        workbook = self.benchmarking_engine.generate(workbook)

        workbook = self.scoring_engine.generate(workbook)

        workbook = self.storytelling_engine.generate(workbook)

        workbook = self.prediction_engine.generate(workbook)

        workbook = self.executive_score_engine.generate(workbook)

        workbook = self.executive_alert_engine.generate(workbook)

        workbook = self.opportunity_engine.generate(workbook)

        workbook = self.risk_engine.generate(workbook)

        workbook = self.forecasting_ai_engine.generate(workbook)

        workbook = self.dashboard_builder_engine.generate(workbook)

        workbook = self.narrative_engine.generate(workbook)

        workbook = self.ai_summary_engine.generate(workbook)

        workbook = self.executive_reporting_engine.generate(workbook)

        return workbook

    # --------------------------------------------------

    def find_primary_keys(self, columns):

        keywords = [

            "id",

            "code",

            "number",

            "no",

            "key"

        ]

        return [

            column

            for column in columns

            if any(

                keyword in column.lower()

                for keyword in keywords

            )

        ]

    # --------------------------------------------------

    def find_date_columns(self, columns):

        keywords = [

            "date",

            "month",

            "year",

            "time"

        ]

        return [

            column

            for column in columns

            if any(

                keyword in column.lower()

                for keyword in keywords

            )

        ]

    # --------------------------------------------------

    def find_numeric_columns(self, sample_data):

        if not sample_data:

            return []

        numeric_columns = []

        first_row = sample_data[0]

        for column, value in first_row.items():

            if isinstance(value, (int, float)):

                numeric_columns.append(column)

                continue

            try:

                float(value)

                numeric_columns.append(column)

            except:

                pass

        return numeric_columns