Tmux is a very powerful terminal multiplexer when you are using the remote server via SSH

### Create Session
```bash
tmux new
```
* create session with names
```bash
tmux new -s [session-name]
```

### View Session
* Tmux session information
```bash
tmux ls
```
* Check Tmux session by hitting `Ctrl` + `b` + `s` and hit `q` to exit the information.

### Detach Session
to return to the local terminal 
hitting `Ctrl` + `b` + `d`

### Kill Session
* kill all session from local terminal
```bash
tmux kill-server
```
* kill specifix session
```bash
tmux kill-session -t [session-name]
```

### Attach Session
```bash
tmux a
```

* attach to specifix sessions from local terminal
```bash
tmux attach -t [session-name]
```

### Create/Close Windows
To create a window, in the Tmux terminal, we hit `Ctrl` + `b` + `c`. To kill the current window, in the Tmux terminal, we hit `Ctrl` + `b` + `&` (& is Shift + 7).

### Select Windowns
We select specific by hitting `Ctrl` + `b` + window id

### Create/Close Panes
To split the pane vertically, we hit `Ctrl` + `b` + `%`. 
To split the pane horizontally, we hit `Ctrl` + `b` + `"`. 
To close the current pane, we we hit `Ctrl` + `b` + `x`.

