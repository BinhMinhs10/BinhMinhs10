# Using colab GPU

## 1. Make **app** trong Driver
## 2. Make **Colaboratory** (right click) 
## 3. Set up 
edit > Notebook settings 
![setup](edit.png)
## 4. Xem docs
```bash
Ctrl + alt + p
```
or
insert > code snippet
## 5. Mount Driver
```bash
from google.colab import drive
drive.mount('/gdrive')
```
After that enter authorization by click URL go get password
## 6. cd 
```bash
import os
os.chdir("/gdrive/My Drive/app")
```
![mount](mount.png)

## 7. Extension Jypyter
[Jupyter Extension](https://towardsdatascience.com/bringing-the-best-out-of-jupyter-notebooks-for-data-science-f0871519ca29)
### Installation
```bash
conda install -c conda-forge jupyter_nbextensions_configurator
```
### Configurable
* Hinterland: giúp autocomplete
* Split Cells Notebook
* Table of contents
* Collapsiable Headings
* Autopep8
* Embedding URLs, PDFs

