from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk,ngrams

def nlp():

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code

    soup = BeautifulSoup(plain_text, "html.parser")
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.getText()

    file1 = open("data.txt","w")
    file1.write(visible_text)

    visible_text1 = open("data.txt").read()
    stokens = nltk.sent_tokenize(visible_text1)
    wtokens = nltk.word_tokenize(visible_text1)

    for s in stokens:
        print(s)
    for w in wtokens:
        print(w)

    file2 = open("stem.txt", "w")
    ps = PorterStemmer()
    for w in wtokens:
        stem = ''.join(ps.stem(w))
        file2.write(stem)
        file2.write("\n")

    file3 = open("lemma.txt", "w")
    lemmatizer = WordNetLemmatizer()
    for l in wtokens:
        lem = lemmatizer.lemmatize(l,pos="a")
        file3.write(lem)
        file3.write("\n")

    file4 = open("POS.txt","w")
    for pos in stokens:
        words = nltk.word_tokenize(pos)
        tagged = nltk.pos_tag(words)
        value = str(tagged)
        file4.write(value)
        file4.write("\n")

    file5 = open("NER.txt", "w")
    for ner in stokens:
        words1 = nltk.word_tokenize(ner)
        tagged1 = nltk.pos_tag(words1)
        chnk = ne_chunk(tagged1)
        value = str(chnk)
        file5.write(value)
        file5.write("\n")

    file6 = open("ngrams.txt", "w")
    for s in stokens:
        words2 = nltk.word_tokenize(s)
        grams = ngrams(words2,3)
        for g in grams:
            file6.write(str(g))
            file6.write("\n")

nlp()



