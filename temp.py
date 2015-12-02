
import re
import newspaper
import urllib
from newspaper import Article
import nltk
import time
#article.authors
cnn_paper = newspaper.build('http://www.cnn.com/tech')

while(0<1):
    print("Started")
    try:
        for article in cnn_paper.articles:
            print(article.url)
        cnn_paper.size()
        time.sleep(5)
        for category in cnn_paper.category_urls():
            print(category)
        time.sleep(60)
        article = cnn_paper.articles[0]
    except:
        continue
    else:
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
        print ("Sleeping for 10 minutes now")
        time.sleep(60)
