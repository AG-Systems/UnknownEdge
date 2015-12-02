
import re
import newspaper
import urllib
from newspaper import Article
import nltk


page = urllib.urlopen("http://xauriga.com/tech.html").read()
summary = "hello my name is "
newsummary = ''.join(('<p> ',summary, '</p>'))
text = re.sub('<p>.*?</p>', newsummary , page)

print text
