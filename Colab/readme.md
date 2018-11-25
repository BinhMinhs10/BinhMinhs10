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
