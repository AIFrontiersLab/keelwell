"""Extension points: stage factories and lifecycle hooks."""

from distributed_training_anatomy.plugins.hooks import HookManager
from distributed_training_anatomy.plugins.registry import StageRegistry

__all__ = ["HookManager", "StageRegistry"]
