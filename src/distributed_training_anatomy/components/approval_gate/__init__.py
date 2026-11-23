"""Approval Gate.

Routes runs touching restricted material to a human approver before release.
"""

from distributed_training_anatomy.components.approval_gate.adapter import ROLE, build
from distributed_training_anatomy.components.approval_gate.config import CONFIG, ApprovalGateConfig
from distributed_training_anatomy.components.approval_gate.errors import ApprovalGateError
from distributed_training_anatomy.components.approval_gate.service import ApprovalGateService

__all__ = ["CONFIG", "ROLE", "build", "ApprovalGateConfig", "ApprovalGateError", "ApprovalGateService"]
