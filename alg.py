
import re
import newspaper
import urllib
from newspaper import Article
import nltk
import time

cnn_paper = newspaper.build('http://cnn.com')

while(0<1):
    for article in cnn_paper.articles:
        print(article.url)
    for category in cnn_paper.category_urls():
        print(category)
    time.sleep(60)
    article = cnn_paper.articles[0]
    article.download()
    time.sleep(10)
    article.parse()
    time.sleep(10)
    article.nlp()
    time.sleep(10)
    summary = article.summary
    page = urllib.urlopen("http://xauriga.com/tech.html").read()
    text_file = open("tech.html", "w")
    newsummary = ''.join(('<p> ',summary, '</p>'))
    text = re.sub('<p>.*?</p>', newsummary , page)
    print text
    text_file.write(text)
    text_file.close()
    time.sleep(600)
