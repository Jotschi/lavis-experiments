#!/bin/bash

set -o nounset
set -o errexit

GPU=$1

SOURCE=output
TARGET=refine

function refineAll() {
  for chunk in $(ls $SOURCE | grep train | shuf) ; do    
    local chunkLock="/tmp/.lock_$chunk"
    if [ -e "$TARGET/$chunk" ] ; then
      echo "[$chunk / $GPU] - Already refined "
      continue
    fi
    if [ -e "$chunkLock" ] ; then
      echo "[$chunk / $GPU] - Locked!"
      continue
    fi
    echo "[$chunk / $GPU] - Invoking refine"
    touch $chunkLock
    . venv/bin/activate
    python3 coco-mistral-converer.py refine "$SOURCE/$chunk" $GPU
    rm $chunkLock
  done
}

refineAll