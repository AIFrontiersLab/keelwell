"""Document source used when a request arrives without pre-retrieved candidates."""

from __future__ import annotations

from typing import Protocol

from distributed_training_anatomy.domain.models import Candidate


class CorpusRepository(Protocol):
    def search(self, query: str, *, tenant: str, limit: int) -> list[Candidate]: ...

    def upsert(self, candidate: Candidate) -> None: ...

    def __len__(self) -> int: ...
