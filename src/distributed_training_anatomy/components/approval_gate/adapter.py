"""Port and registry adapter for Approval Gate.

Interface from the architecture specification: ``approve(run_id, approver) -> token``
"""

from __future__ import annotations

from typing import Protocol

from distributed_training_anatomy.components.approval_gate.config import CONFIG
from distributed_training_anatomy.components.approval_gate.service import ApprovalGateService
from distributed_training_anatomy.domain.models import PipelineContext

ROLE = CONFIG.role


class ApprovalGatePort(Protocol):
    """Contract the orchestrator relies on."""

    name: str
    role: str

    def process(self, ctx: PipelineContext) -> None: ...

    def describe(self) -> dict: ...


def build(services) -> ApprovalGateService:
    return ApprovalGateService(services)
