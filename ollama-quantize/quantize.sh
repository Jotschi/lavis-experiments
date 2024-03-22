#!/bin/bash

MODEL=r256-b4-a16-seq512-l2.0e-5_prefix-8500

#--vocabtype bpe \
docker run --rm -v "$(pwd)/../mistral-deepspeed/models/$MODEL/:/model" ollama/quantize \
    -q q4_0 \
     /model
