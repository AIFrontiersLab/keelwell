"""Role implementations. Components specialise one of these strategies."""

from distributed_training_anatomy.stages.answer import AnswerStage
from distributed_training_anatomy.stages.approval import ApprovalStage
from distributed_training_anatomy.stages.audit import AuditStage
from distributed_training_anatomy.stages.base import Stage, StageServices
from distributed_training_anatomy.stages.budget import BudgetStage
from distributed_training_anatomy.stages.cache import CacheStage
from distributed_training_anatomy.stages.enrich import EnrichStage
from distributed_training_anatomy.stages.fallback import FallbackStage
from distributed_training_anatomy.stages.ingest import IngestStage
from distributed_training_anatomy.stages.policy import PolicyStage
from distributed_training_anatomy.stages.retrieve import RetrieveStage
from distributed_training_anatomy.stages.score import ScoreStage

ROLE_CLASSES: dict[str, type[Stage]] = {
    "ingest": IngestStage,
    "retrieve": RetrieveStage,
    "enrich": EnrichStage,
    "score": ScoreStage,
    "cache": CacheStage,
    "policy": PolicyStage,
    "budget": BudgetStage,
    "approval": ApprovalStage,
    "fallback": FallbackStage,
    "audit": AuditStage,
    "answer": AnswerStage,
}

__all__ = ["ROLE_CLASSES", "Stage", "StageServices", *[cls.__name__ for cls in ROLE_CLASSES.values()]]
