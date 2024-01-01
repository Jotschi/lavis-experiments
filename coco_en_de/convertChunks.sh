#!/bin/bash

set -o nounset
set -o errexit

GPU=$1

function convertRemaining() {
  for chunk in $(ls chunks | shuf) ; do
    local chunkLock="/tmp/.lock_opus_$chunk"
    if [ -e "output/$chunk" ] ; then
      echo "[$chunk / $GPU] - Already converted "
      continue
    fi
    if [ -e "$chunkLock" ] ; then
      echo "[$chunk / $GPU] - Locked!"
      continue
    fi
    echo "[$chunk / $GPU] - Invoking converter"
    touch $chunkLock
    . venv/bin/activate
    python3 coco-converter.py translate "chunks/$chunk" $GPU
    rm $chunkLock
  done
}

convertRemaining
