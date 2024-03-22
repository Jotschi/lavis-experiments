#!/bin/bash

VERSION=0.1.29
NAME="ollama-create"

docker rm -f $NAME
docker run -d --rm \
    --name $NAME \
    -v "$(pwd)/models:/models" \
    ollama/ollama:$VERSION

docker exec -it $NAME /bin/bash
    # cd /models/mistral7b-prefix-model
    # ollama create mistral7b-prefix-model
    # ollama run mistral7b-prefix-model