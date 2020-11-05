# Tips usefull with console

## Author
   **BinhMinhs10**
### 1. List & Kill all with string 'firefox' in command
```bash
pgrep -fl firefox && pkill -f firefox
```
### 2. Open port ubuntu
```bash
sudo ufw allow 7000
sudo ufw allow 10000:10050
```
### 3. Cleaning disk space
* filter by file size
```bash
du -h /home/user/source_Python/ | grep '^\s*[0-9\.]\+G'
```