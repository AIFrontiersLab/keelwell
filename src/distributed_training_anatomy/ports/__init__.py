"""Ports: the interfaces the application core requires from the outside world.

Adapters under ``distributed_training_anatomy.adapters`` implement these protocols. The core never
imports an adapter directly; the composition root (``container.py``) wires them.
"""

from distributed_training_anatomy.ports.audit import AuditSink
from distributed_training_anatomy.ports.cache import RankingCache
from distributed_training_anatomy.ports.corpus import CorpusRepository
from distributed_training_anatomy.ports.event_bus import EventBus
from distributed_training_anatomy.ports.repository import RunRepository
from distributed_training_anatomy.ports.scorer import RelevanceScorer

__all__ = ["AuditSink", "CorpusRepository", "EventBus", "RankingCache", "RelevanceScorer", "RunRepository"]
