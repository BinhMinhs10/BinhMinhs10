# Tips usefull with git 

## Practice online [8 tips use git](https://topdev.vn/blog/lam-viec-voi-github/?fbclid=IwAR28B8PRFZbvbQl3JqXsDDjo7RKHtsYmaLRBJBCauWSsBHT49UQv7rMuuc0)

## Author
   **Binh Minh**
### 1. Tìm kiếm file nhanh trong Repository
Ấn phím 't' trong repository
### 2. Xem Repo theo thư mục dạng cây
Cài extension [Octotree extension](https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc) trên Chrome

### 3. Xem lịch sử thay đổi file 
Git blame hoặc dùng ấn phím 'b' trên màn hình
### 4. Phím tắt vào search trên git 
Ấn phím '/'

## Git Command [Youtube](https://www.youtube.com/watch?v=HVsySz-h9r4&list=PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx)

### 5. Xem lịch sử commit (author+message+date) trên remote
```bash
git log --pretty=oneline
```
or show 5 most recent commits
```bash
git log --oneline --graph -5
```
### 6. Xem thông tin trên remote repository
- information on remote
$ git remote -v
- list all branch on remote
$ git branch -a 
### 7. Xóa branch
```bash
$ git branch -d name_branch 
$ git push origin --delete name_branch
```
### 8. Edit message affter commit
$ git commit --amend -m "message"
### 9. Revert 
$ git revert head_hash
### 10. Revert file after delete in local 
* this restores the file status in the index
```bash
$ git reset -- <file>
```
* then discard changes in working directory
```bash
$ git checkout -- <file>
```
### 11. Alias git commands
```bash
git config --global alias.show-graph 'log --graph --pretty=oneline'
git show-graph
```
### 12. Empty message option
```bash
git commit --allow-empty-message -m ""
```
