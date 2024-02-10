#!/bin/bash

# Host Env
sudo apt-get install gcc-12 gcc-11 g++-11
sudo apt-get install  libaio-dev libaio1

# Python
python3.11 -m venv venv
. venv/bin/activate
pip install torch torchvision torchaudio 
pip install datasets
pip install transformers happytransformer

git clone https://github.com/Xirider/finetune-gpt2xl
git clone https://github.com/microsoft/DeepSpeed -b v0.12.6
pip install --upgrade pip

exit 0
CUDA_VISIBLE_DEVICES=0

cd DeepSpeed
S_BUILD_OPS=1 pip install .
#ds_report
#DeepSpeed
cd finetune-gpt2xl
deepspeed --num_gpus=1 run_clm.py
    --deepspeed ds_config_gptneo.json,
    --model_name_or_path EleutherAI/gpt-neo-1.3B,
    --train_file train.csv,
    --validation_file validation.csv,
    --do_train,
    --do_eval,
    --fp16,
    --overwrite_cache,
    --evaluation_strategy=steps,
    --output_dir finetuned,
    --num_train_epochs 1,
    --eval_steps 15,
    --gradient_accumulation_steps 2,
    --per_device_train_batch_size 4,
    --use_fast_tokenizer False,
    --learning_rate 5e-06,
    --warmup_steps 10

