#!/bin/bash

set -o nounset
set -o errexit

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

. $SCRIPT_DIR/.venv/bin/activate

export CUDA_VISIBLE_DEVICES=0
accelerate launch --config_file=$SCRIPT_DIR/deepspeed_zero3.yaml --gradient_accumulation_steps 8 "$SCRIPT_DIR/sft_trainer_awq.py"
