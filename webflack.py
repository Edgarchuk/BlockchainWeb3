from  __init__ import *
from flask import Flask, request,render_template

app = Flask(__name__)
global imagedab
global sitep
imagedab = './image/'
sitep = '/site/'

startl()

@app.route('/newimage',methods = ["GET","POST"] )
def NewIm():
    if request.method == "POST":
        file = request.files["file"]
        if TFBD() == True:
            with open(imagedab + file.filename,'w') as f:
                f = file
        NewBlock(file.filename,Hashfiles(imagedab + file.filename))
    return '''
        <form action="/newimage" method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Загрузить</button>
        </form>'''
@app.route('/index')
def index():
    s = ''
    if TFBD() == True:
        l = os.listdir(path=blockchaindeb)
        files = []
        for q in l:
            files.append(int(q))
        files = sorted(files)
        del l
        if files[-1] > 1:
            i = 2
            while i <= len(files):
                with open(blockchaindeb + '/' + str(i), 'r') as f:
                    l = json.loads(f.read())
                    s += 'Name: ' + l["name"] + ' hash: ' + l["ihash"] + '\n'
                i += 1
    return s

if __name__ == '__main__':
    app.run(debug=True)