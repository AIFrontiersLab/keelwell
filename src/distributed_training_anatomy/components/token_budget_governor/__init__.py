"""Token Budget Governor.

Enforces per-request and global token ceilings before evidence reaches the answer stage.
"""

from distributed_training_anatomy.components.token_budget_governor.adapter import ROLE, build
from distributed_training_anatomy.components.token_budget_governor.config import CONFIG, TokenBudgetGovernorConfig
from distributed_training_anatomy.components.token_budget_governor.errors import TokenBudgetGovernorError
from distributed_training_anatomy.components.token_budget_governor.service import TokenBudgetGovernorService

__all__ = ["CONFIG", "ROLE", "build", "TokenBudgetGovernorConfig", "TokenBudgetGovernorError", "TokenBudgetGovernorService"]
