#!/bin/bash

set -o nounset
set -o errexit

jq -s 'reduce .[] as $x ([]; . + $x)' $1/*
