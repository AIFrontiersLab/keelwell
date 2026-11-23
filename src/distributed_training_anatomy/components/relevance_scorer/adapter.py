"""Port and registry adapter for Relevance Scorer.

Interface from the architecture specification: ``score(query, candidate) -> float``
"""

from __future__ import annotations

from typing import Protocol

from distributed_training_anatomy.components.relevance_scorer.config import CONFIG
from distributed_training_anatomy.components.relevance_scorer.service import RelevanceScorerService
from distributed_training_anatomy.domain.models import PipelineContext

ROLE = CONFIG.role


class RelevanceScorerPort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> RelevanceScorerService:
    return RelevanceScorerService(services)
