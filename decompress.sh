#!/bin/sh

for user in $( rm exploded/**/wiki_* )
do
  bunzip2 $user
done
