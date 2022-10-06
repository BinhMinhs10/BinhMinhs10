
* 
```bash
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM
```


```bash
/usr/bin/gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
/usr/bin/gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM
```


* Install Nvidia Driver Same as with the above standard Ubuntu repository
```bash
sudo ubuntu-drivers autoinstall
sudo apt install nvidia-driver-470
sudo reboot
```

## cuDNN
* The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. cuDNN provides highly tuned implementations for standard routines such as forward and backward convolution, pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep Learning SDK.
* install `nvidia-cudnn` on Ubuntu 22.04
```bash
sudo apt -y install nvidia-cudnn
```