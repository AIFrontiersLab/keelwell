"""Signal Enricher.

Annotates candidates with token counts and query overlap, and collapses duplicate passages.
"""

from distributed_training_anatomy.components.signal_enricher.adapter import ROLE, build
from distributed_training_anatomy.components.signal_enricher.config import CONFIG, SignalEnricherConfig
from distributed_training_anatomy.components.signal_enricher.errors import SignalEnricherError
from distributed_training_anatomy.components.signal_enricher.service import SignalEnricherService

__all__ = ["CONFIG", "ROLE", "build", "SignalEnricherConfig", "SignalEnricherError", "SignalEnricherService"]
