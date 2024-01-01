# Tiny Stories

* Branch: https://github.com/Jotschi/LAVIS/tree/dev-tinystories


## QFormer Training

```bash
. venv/bin/activate
export CUDA_VISIBLE_DEVICES=0
torchrun train.py --cfg-path lavis/projects/blip2/train/pretrain_stage2_tinystories33m.yaml
```

## Distributed QFormer Training

```bash
. venv/bin/activate
export CUDA_VISIBLE_DEVICES=0
python -m torch.distributed.run --nproc_per_node=1 train.py --cfg-path lavis/projects/blip2/train/pretrain_stage2_tinystories33m.yaml
```
