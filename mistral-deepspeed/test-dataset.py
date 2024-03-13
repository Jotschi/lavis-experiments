from datasets import load_dataset

dataset_name = "Jotschi/coco-karpathy-opus-de"
coco_dataset = load_dataset(dataset_name)


def chunk_examples(batch):
    all_captions = []
    for captions in batch["caption"]:
        for caption in captions:
            all_captions += [caption]
    return {"caption": all_captions}

print(coco_dataset)
chunked_dataset = coco_dataset.map(chunk_examples, batched=True, num_proc=4,
                                   remove_columns=["image_id", "caption", "image"])
print(chunked_dataset)
print(len(chunked_dataset['train']))

print(chunked_dataset['train'][0])
print(chunked_dataset['train'][1])
