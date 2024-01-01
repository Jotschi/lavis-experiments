# Python 3.10

```bash
sudo apt-get install lzma
sudo apt install libncurses-dev libgdbm-dev libz-dev tk-dev libsqlite3-dev libreadline-dev liblzma-dev libffi-dev build-essential zlib1g-dev libncurses5-dev libnss3-dev libssl-dev wget libbz2-dev

cd /opt/python
wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz
unp Python-3.10.13.tgz
mv Python-3.10.13 python-3.10.13

cd python-3.10.13
./configure --enable-optimizations
make -j 2

sudo rm /usr/local/bin/python310 
sudo ln -s /opt/python/python-3.10.13/python /usr/local/bin/python310

python310 -m pip install ipykernel -U --user --force-reinstall
python310 -m ensurepip --default-pip 
```
