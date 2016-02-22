#!/bin/sh

for user in $( find data -name "*.bz2")
do
  bunzip2 $user
done
