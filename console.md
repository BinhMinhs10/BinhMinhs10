# Tips usefull with console

## Author
   **BinhMinhs10**
### 1. List & Kill all with string `firefox` in command
```bash
pgrep -fl firefox && pkill -f firefox
```
* Show device in RAM memory
```bash
sudo dmidecode --type 17
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
### 4. Pip Guide
* Remove all items from the cache pip.
```bash
python -m pip cache list
python -m pip cache purge
```
### 5. Search word in folder
```bash
grep -nr 'ㅎ' .
```
### 6. virtualenv
* create and active virtualenv
```bash
virtualenv -p python3 venv
source venv/bin/activate
```