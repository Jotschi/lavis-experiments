# COCO Mistral7B ReCaption for TinyStories (33M) LLM

This folder contains tools that were used to modify the original COCO captions to be more suitable to be used in combination with the TinyStories (33M) LLM which uses a reduced corpus. The captions were rephrased into very simple english so that a young child would understand it.

Process:

* Split original annotations file into chunks of 5000 captions each using `split-coco.sh`.
* Run `coco-caption-converter.py caption [chunkfile] [gpuId]` on each chunk file to generate captions that are more suitable for TinyStories LLM.
* Run `coco-caption-converter.py refine [chunkfile] [gpuId]` on the output of `caption` to re-generate captions that don't match defined quality gate. (Single line of text, No explentations, No introduction, No Ascii Art)
* Merge chunks back into one file using `merge-coco.sh`.
