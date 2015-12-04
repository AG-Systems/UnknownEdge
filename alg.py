
import re
import newspaper
import urllib
from newspaper import Article
import nltk
import time

str1 = '<p>'
str2 = '</p>'

cnn_paper = newspaper.build('http://abcnews.go.com/')
n = 0
while(0<1):
    try:
        for article in cnn_paper.articles:
            print(article.url)
        for category in cnn_paper.category_urls():
            print(category)
        time.sleep(10)
        article = cnn_paper.articles[n]
        print "Started the article download"
        article.download()
        print "Article finished the download"
        time.sleep(10)
        print "Started the parse"
        article.parse()
        print "Finished the parse"
        time.sleep(10)
        print "Started the nlp"
        article.nlp()
        print "Finished the nlp"
        time.sleep(10)
        summary = article.summary
        print summary
        page = urllib.urlopen("http://xauriga.com/tech.html").read()
        text_file = open("tech.html", "w")
        print "Opened tech.html"
        newsummary = ''.join(('<p> ',summary, '</p>'))
        print newsummary
        reg = "%s(.*?)%s" % (str1,str2)
        r = re.compile(reg,re.DOTALL)
        result = r.sub(newsummary, page)
        #text = re.sub('<p>.*?</p>', newsummary , page)
        print result
        text_file.write(result)
        text_file.close()
        n =+ 1
        time.sleep(5)
    except:
        print "Error. Re-try "
        pass
    
