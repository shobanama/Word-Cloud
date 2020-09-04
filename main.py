from flask import Flask,request
from blogic import *
import datetime
import sys
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"


@app.route('/wordtrend')
def find_wordtrend():
    #res=displayText()
    status="False"
    top_n_words=0
    n = len(sys.argv)
    top_n_words=0
    if n==2:
        top_n_words=int(sys.argv[1])

    try:
        taburl = request.args.get('taburl')
        fname=''
        fname=taburl[taburl.rfind('/')+1:].replace('.pdf','')
        dt = datetime.datetime.now().strftime("_%Y%m%d_%H%M%S")
        fname=fname+dt
        print('filename:',fname)

        content=parsingurl(taburl,fname)
        if len(content)>1:
            status=create_wordcloud(content,fname)
            find_most_fequent_word(content,top_n_words,fname)

        else:
            print('lenght of text is insufficient ot make word cloud')
    except Exception as e:
        print(e)

    return status



if __name__ == '__main__':
   app.run()
