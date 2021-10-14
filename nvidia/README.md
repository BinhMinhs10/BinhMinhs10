# SETUP
## Bug 
* Could not load dynamic library 'libcusolver.so.10'; dlerror: libcusolver.so.10
```bash
sudo ln -s /usr/local/cuda/lib64/libcusolver.so.11 /usr/local/cuda/lib64/libcusolver.so.10
export LD_LIBRARY_PATH=/usr/local/cuda/lib64
```
* Tensorfow list device
```python
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

## Uninstall Nvidia Driver

Purge Nvidia Packages
```bash
dpkg -l | grep -i nvidia
sudo apt-get remove --purge '^nvidia-.*'
sudo apt autoremove
sudo apt-get install ubuntu-desktop
sudo /usr/bin/nvidia-uninstall
```