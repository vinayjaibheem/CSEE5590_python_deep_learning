from bs4 import BeautifulSoup
import urllib.request
import nltk
from collections import defaultdict
import collections,operator
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk,ngrams

def nlp():

    url = "https://en.wikipedia.org/wiki/Emotion"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code

    soup = BeautifulSoup(plain_text, "html.parser")
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.getText()

    file1 = open("input.txt","w")
    file1.write(visible_text)

    visible_text1 = open("input.txt").read()
    wtokens = nltk.word_tokenize(visible_text1)
    stokens = nltk.sent_tokenize(visible_text1)
#Applying lemmatization

    file1 = open("lemma.txt", "w")
    lemmatizer = WordNetLemmatizer()
    for l in wtokens:
        lem = lemmatizer.lemmatize(l, pos="a")
        file1.write(lem)
        file1.write("\n")

#Applying bigram on the text

    file2 = open("bigrams.txt", "w")
    lns = []
    for s in stokens:
        words2 = nltk.word_tokenize(s)
        grams = ngrams(words2,2)
        for g in grams:
            file2.write(str(g))
            file2.write("\n")
            lns.append(g)

#calculating the frequency of the bigrams

    wrdcnt1 = collections.Counter(lns)
    file3 = open("Bigram_Freq.txt","w")
    file3.write(str(wrdcnt1))
    file3.write("\n")

    print("Finding the top 5 bigrams:")
    print("\n")
    freqc = nltk.FreqDist(lns)
    mcommon = freqc.most_common(5)

    # Printing top five bigrams which are discovered utilizing most_common work.
    print(mcommon)

   #find sentences with most repeated bigram

    with open('input.txt', 'r') as file:
        length = file.readlines()
    val = ''

    for i in length:
        val = val + i
    sen = nltk.sent_tokenize(val)
    rep_sent1 = []

    for sentences in sen:
        for word, wrd1 in lns:
            for ((cp, val), l) in mcommon:
                if (word, wrd1 == cp, val):
                    rep_sent1.append(sentences)

    # best five biagrams sentences
    print("\n Printing lines with top five bigrams")
    fc = nltk.FreqDist(rep_sent1)
    fff = fc.most_common(5)
    app_sent = []
    for ke, val in fff:
        app_sent.append(ke)
    print(app_sent)
nlp()
