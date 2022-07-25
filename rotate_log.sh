#!/bin/bash

dir="/home/gm4slv/PythonProjects/sandbox"
date=`date +%y-%m-%d_%H%M%S_`
file="logfile.txt"

newfile=$date$file

mv $dir/$file $dir/$newfile

touch $dir/$file

gzip  $dir/$newfile
