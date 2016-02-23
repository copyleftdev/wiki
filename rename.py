import os
import uuid

path = "data"

for(dirpath, dirname, files) in os.walk(path):
    for filename in files:
        filepath = os.path.join(dirpath, filename)
        os.rename(filepath,'{}.txt'.format(filepath))
