# Easy install PyPy3

## install PyPy3 on ubuntu
```bash
sudo add-apt-repository ppa:pypy/ppa
sudo apt update
sudo apt install pypy3
```

## install/upgrade pip
```bash
pypy3 -m ensurepip
pypy3 -m pip install --upgrade pip setuptools wheel
pypy3 -m pip install numpy
```
