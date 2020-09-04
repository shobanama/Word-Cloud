
import PyPDF2
import re
from urllib.request import urlopen
# Python program to generate WordCloud
# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def download_file(download_url,filename):
    response = urlopen(download_url)
    with open('pdfs/'+filename+'.pdf', 'wb') as file:
        file.write(response.read())
        file.close()
        print('This pdf is downloaded sucessfully')



def parsingurl(pdfurl,filename):
    # creating a pdf file object
    dataset=''
    if pdfurl.startswith("file:"):
        pdfurl=pdfurl.replace('file:///','')
    elif pdfurl.startswith("https:"):
        download_file(pdfurl,filename)
        pdfurl='pdfs/'+filename+'.pdf'


    pdfFileObj = open(pdfurl, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages=pdfReader.numPages
    print("total_pages",pages)
    print('====================================')
    # creating a page object

    for page in range(0,pages):
        pageObj = pdfReader.getPage(page)
        dataset=dataset+pageObj.extractText()


    pdfFileObj.close()
    return dataset

def create_wordcloud(dataset,filename):
    length=len(dataset)
    status="False"
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = set(STOPWORDS),
                min_font_size = 10).generate(dataset)
    wordcloud.to_file("images/WordCloud.png")
    status="True"
    return status

def find_most_fequent_word(dataset,top_n_words,filename):
    wc = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = set(STOPWORDS),
                min_font_size = 10).process_text(dataset)
    #print(wc)

    if top_n_words==0 or top_n_words>len(wc):
        top_n_words=len(wc)
    with open('words/'+filename+'.txt', 'w') as file:
        for k, v in sorted(wc.items(), key=lambda item: item[1],reverse=True)[:top_n_words]:
            file.write(str(k)+","+str(v)+"\n")




#d=parsingurl(r'https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45530.pdf')
#create_wordcloud(d)
