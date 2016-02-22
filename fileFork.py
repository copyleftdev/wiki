from BeautifulSoup import BeautifulSoup
import uuid

path = 'articles'

with open('sample.txt','r') as myfile:
    #data = myfile.read()


    test = BeautifulSoup(myfile.read())
    getdocs = test.findAll('doc')
    for item in getdocs:
        with open('{}/{}.txt'.format(path,uuid.uuid4()),'w') as genfile:
            genfile.write(str(item))
