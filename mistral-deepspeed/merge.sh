#!/bin/bash

set -o nounset
set -o errexit


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

. $SCRIPT_DIR/venv/bin/activate


NAME=checkpoint-1500

python merge_peft_adapter.py \
    peft_model_path=output/$NAME \
    output_dir=models/$NAME \
    base_model_name_or_path=mistralai/Mistral-7B-v0.1

