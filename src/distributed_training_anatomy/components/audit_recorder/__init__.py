"""Audit Recorder.

Writes a hash-chainable audit record for every run, including denials and degradations.
"""

from distributed_training_anatomy.components.audit_recorder.adapter import ROLE, build
from distributed_training_anatomy.components.audit_recorder.config import CONFIG, AuditRecorderConfig
from distributed_training_anatomy.components.audit_recorder.errors import AuditRecorderError
from distributed_training_anatomy.components.audit_recorder.service import AuditRecorderService

__all__ = ["CONFIG", "ROLE", "build", "AuditRecorderConfig", "AuditRecorderError", "AuditRecorderService"]
