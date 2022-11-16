#!/bin/bash

posts=$(ls -r posts)

p=(posts/*)

first="${p[0]}"

file_list="template/pre.html"

for f in ${posts}
do
    file_list+=" posts/$f"
    if [[ "posts/$f" == "$first" ]]
    then
	break
    fi
    file_list+=" template/line.txt"
done

file_list+=" template/post.html"

cat $file_list
