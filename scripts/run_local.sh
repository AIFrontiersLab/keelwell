#!/usr/bin/env bash
set -euo pipefail
export DISTRIBUTED_TRAINING_ANATOMY_CONFIG=${DISTRIBUTED_TRAINING_ANATOMY_CONFIG:-config/development.toml}
PYTHONPATH=src exec python -m distributed_training_anatomy serve "$@"
