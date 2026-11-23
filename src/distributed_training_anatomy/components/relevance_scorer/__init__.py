"""Relevance Scorer.

Scores query-candidate relevance with a deterministic BM25-style reference model.
"""

from distributed_training_anatomy.components.relevance_scorer.adapter import ROLE, build
from distributed_training_anatomy.components.relevance_scorer.config import CONFIG, RelevanceScorerConfig
from distributed_training_anatomy.components.relevance_scorer.errors import RelevanceScorerError
from distributed_training_anatomy.components.relevance_scorer.service import RelevanceScorerService

__all__ = ["CONFIG", "ROLE", "build", "RelevanceScorerConfig", "RelevanceScorerError", "RelevanceScorerService"]
