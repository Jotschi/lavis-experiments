#!/bin/bash

export CC=/usr/bin/gcc-11

cd finetune-tinystories

#accelerate launch
deepspeed --num_gpus=1 run_clm.py \
--deepspeed ds_config_gptneo.json \
--model_name_or_path roneneldan/TinyStories-33M \
--train_file train.csv \
--validation_file validation.csv \
--do_train \
--do_eval \
--fp16 \
--overwrite_cache \
--evaluation_strategy="steps" \
--output_dir finetuned \
--num_train_epochs 300 \
--eval_steps 150 \
--gradient_accumulation_steps 2 \
--per_device_train_batch_size 4 \
--use_fast_tokenizer False \
--learning_rate 5e-06 \
--warmup_steps 100

#--keep_last_n_checkpoints=3 \
#--save_interval=10_000 \