import json
import os
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

global blockchaindeb
blockchaindeb = './blockchain'

class Handleader(FileSystemEventHandler):
    def on_deleted(self, event):
        print(event)
    def on_created(self, event):
        print(event)
    def on_moved(self, event):
        print(event)

def Hashfiles(filename: str) -> str:
    with open(filename,'rb') as fd:
        h = hashlib.new('sha256')
        h.update(fd.read())
    return  h.hexdigest()


def NewBlock(text = '',ihash = ''):
    if TFBD() == True:
        l = os.listdir(path=blockchaindeb)
        files = []
        for q in l:
            files.append(int(q))
        files = sorted(files)
        del l
        BN = files[-1]
        BHash = Hashfiles(blockchaindeb + '/' + str(BN))
        with open(blockchaindeb + '/'+ str(BN + 1),'w') as f:
            f.write(json.dumps({'name': text, 'Bhash': BHash, 'ihash': ihash}, indent=4))


def TFBD() -> bool:
    l = os.listdir(path=blockchaindeb)
    files = []
    for q in l:
        files.append(int(q))
    files = sorted(files)
    del l
    w = True
    if files[-1] > 1:
        i = 2 
        while i <= len(files):
            with open(blockchaindeb + '/' + str(i),'r') as f:
                l = json.loads(f.read())
                Hashn = l["Bhash"]
            if Hashfiles(blockchaindeb + '/' + str(i - 1)) == Hashn:
                print('in {}: Correct'.format(i))
            else:
                w = False
                print('in {}: Error'.format(i))
            i += 1

    return w

def Getname(numder: int) -> str:
    with open(blockchaindeb + '/' + str(numder)) as f:
        l = json.loads(f.read())
        result = l["name"]
    return result

def Getihash(numder: int) -> str:
    with open(blockchaindeb + '/' + str(numder)) as f:
        l = json.loads(f.read())
        result = l["ihash"]
    return result

def startl():
    observer = Observer()
    observer.schedule(Handleader() , path = blockchaindeb)
    observer.start()
