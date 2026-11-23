"""Typed configuration: defaults in code, profiles in TOML, overrides from the environment."""

from distributed_training_anatomy.config.loader import load_settings
from distributed_training_anatomy.config.settings import Settings

__all__ = ["Settings", "load_settings"]
