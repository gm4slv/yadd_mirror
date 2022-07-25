#!/bin/bash
 
session="mirror"
 
tmux start-server
 
tmux new-session -d -s $session
 
tmux rename-window "yadd_mirror"
 
tmux selectp -t 0
tmux send-keys "python /home/gm4slv/PythonProjects/sandbox/yadd_mirror.py" C-m
