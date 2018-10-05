from bs4 import BeautifulSoup
import urllib.request
import io
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

url = "https://en.wikipedia.org/wiki/Deep_learning"
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()

with io.open("input.txt","w",encoding="utf-8") as file:
    file.write(visible_text)

f = open("input.txt", "r",encoding="utf-8")
fileread = f.read()

tokens = word_tokenize(fileread)
print("Tokenization output:",tokens)

port_stem = PorterStemmer()
stem_list =[]
for w in tokens:
    stem_list.append(port_stem.stem(w))

print("Stemming output: ",stem_list)


