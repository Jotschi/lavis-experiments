# LAVIS Experiments

This repository contains various scripts and docs that I use for my LAVIS experiments.

## Dataset References

The processed COCO datasets in this repo are based on the following sources:

* 941425b651f50cdb1a6f0673eaab6260  vg_caption.json
* aa31ac474cf6250ebb81d18348a07ed8  coco_karpathy_train.json
* 3ff34b0ef2db02d01c37399f6a2a6cd1  coco_karpathy_test.json
* b273847456ef5580e33713b1f7de52a0  coco_karpathy_val.json

## Tiny Stories

`coco_karpathy_simple_english.tar.gz` and `vg_caption_simple_english.tar.gz` contain [MS COCO](https://paperswithcode.com/dataset/coco) and [Visual Genome](https://paperswithcode.com/dataset/visual-genome) caption translations into simplified english.

Used model: TheBloke/Mistral-7B-Instruct-v0.2-AWQ

# German Captions

`coco_karpathy_de.tar.gz` and `vg_de.tar.gz` contain [MS COCO](https://paperswithcode.com/dataset/coco) and [Visual Genome](https://paperswithcode.com/dataset/visual-genome) caption translations into german.

Used model: Helsinki-NLP/opus-mt-en-de