#!/bin/bash

set -o nounset
set -o errexit

CHUNK_SIZE=5000

function help() {
    echo "$0 [source file] [dest folder]"
    exit 10
}

function splitCoco() {
    local source="$1"
    local output="$2"
    local filename="$(basename "$source")"
    local name="${filename%.*}"
    echo "Splitting $source files into $output with size $CHUNK_SIZE"
    mkdir -p "$output"
    jq -c .[] "$source" | split -l $CHUNK_SIZE --additional-suffix=.json - "$output/${name}_"
}

if [ "$#" -ne 2 ] ; then
  help
else
  splitCoco "$1" "$2"
fi