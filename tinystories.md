# Tiny Stories

* Branch: https://github.com/Jotschi/LAVIS/tree/dev-tinystories


## QFormer Training

```bash
export CUDA_VISIBLE_DEVICES=0
. venv/bin/activate
torchrun train.py --cfg-path lavis/projects/blip2/train/pretrain_stage2_tinystories33m.yaml
```