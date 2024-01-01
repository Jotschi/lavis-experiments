# LAVIS

## Setup

```bash
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```


## Dataset Setup

```bash
cd lavis/datasets/download_scripts
python3 -m venv venv
pip3 install --upgrade pip
pip3 install salesforce-lavis
```

### COCO

```bash
cd lavis/datasets/download_scripts
python download_coco.py
```


### Visual Genome

```bash
cd lavis/datasets/download_scripts
python download_vg.py
```
