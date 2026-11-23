"""Distributed Training Anatomy: governed reference service.

Distributed Training Anatomy: Unraveling the Complexities of Large-Scale Model Training

Public entry points:

* ``build_container`` - wire the full object graph from settings.
* ``run`` - execute a single request and return the outcome as a dict.
"""

from distributed_training_anatomy.application.pipeline import run
from distributed_training_anatomy.container import build_container
from distributed_training_anatomy.version import __version__

__all__ = ["__version__", "build_container", "run"]
