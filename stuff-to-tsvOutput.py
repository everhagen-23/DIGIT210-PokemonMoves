import os
import spacy
import re
import pandas as pd

nlp = spacy.load("en_core_web_md")

type = []
desc = []

collPath = "dataDesc"

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = f"{collPath}/{file}"
        moveType, extension = os.path.splitext(file)
        print(moveType)
        with open(filepath, 'r', encoding= 'utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            pattern = re.compile(r'\n.*')
            matches = pattern.findall(readFile)
            for match in matches:
                type.append(moveType)
                desc.append(match)
            data = {
                'Attack Type' : type,
                'Description' : desc
            }
            df = pd.DataFrame(data)
            df.to_csv("desc_output.tsv", sep="\t", index=False)