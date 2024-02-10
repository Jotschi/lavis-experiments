#!/bin/bash

#export PYTORCH_NVCC="/usr/local/cuda/bin/nvcc -allow-unsupported-compiler"
#export CUDA_NVCC_EXECUTABLE="blar"

#export NVCC_FLAGS_EXTRA="-allow-unsupported-compiler"
export CC=/usr/bin/gcc-11

cd finetune-gpt2xl
deepspeed --num_gpus=1 run_clm.py \
--deepspeed ds_config_gptneo.json \
--model_name_or_path EleutherAI/gpt-neo-1.3B \
--train_file train.csv \
--validation_file validation.csv \
--do_train \
--do_eval \
--fp16 \
--overwrite_cache \
--evaluation_strategy="steps" \
--output_dir finetuned \
--num_train_epochs 1 \
--eval_steps 15 \
--gradient_accumulation_steps 2 \
--per_device_train_batch_size 4 \
--use_fast_tokenizer False \
--learning_rate 5e-06 \
--warmup_steps 10

#