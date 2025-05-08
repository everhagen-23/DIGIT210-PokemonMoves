import os
from collections import Counter
import spacy
import re
import pandas as pd

nlp = spacy.load("en_core_web_md")

type = []
desc = []
theFile = []
attack = []
bigWord = []
bigNum = []
btmWord = []
btmNum = []
def wordCollector(words):
    wordList = []
    for token in words:
        if token.text.endswith("ly"):
            wordList.append(token.text)
    return wordList

collPath = "dataDesc"

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = f"{collPath}/{file}"
        moveType, extension = os.path.splitext(file)
        print(moveType)
        with open(filepath, 'r', encoding= 'utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            myWords = wordCollector(spacyRead)
            word_freq = Counter(myWords)
            topTree = word_freq.most_common(3)
            lastTree = word_freq.most_common()[:-4:-1]
            for word, freq in topTree:
                theFile.append(moveType)
                attack.append(moveType)
                bigWord.append(word)
                bigNum.append(freq)
            for word,freq in lastTree:
                btmWord.append(word)
                btmNum.append(freq)
            pattern = re.compile(r'\n.*')
            matches = pattern.findall(readFile)
            for match in matches:
                type.append(moveType)
                desc.append(match)
            data = {
                'Attack Type' : type,
                'Description' : desc
            }
            moreData = {
                'Attack Type' : theFile,
                'From File' : attack,
                'Top Five Words' : bigWord,
                'Top Amount Used' : bigNum,
                'Bottom Three Words' : btmWord,
                'Bottom Amount Used' : btmNum
            }
            dmf = pd.DataFrame(moreData)
            dmf.to_csv("MoreData_output.tsv", sep="\t", index=False)
            #df = pd.DataFrame(data)
            #print(df)
            #df.to_csv("desc_output.tsv", sep="\t", index=False)