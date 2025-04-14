import bs4
from lxml import etree
from lxml import html
import os

collPath = "data"

for file in os.listdir(collPath):
    if file.endswith(".html"):
        filepath = f"{collPath}/{file}"
        name, extension = os.path.splitext(file)
        print(name)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            # lengthFile = len(readFile)
            # print(lengthFile)
            tree = html.fromstring(readFile)
            tableRows = tree.xpath('//table[@id="moves"]//tr')
            for row in tableRows:
                moveName = row.xpath('td[1]/a[@class="ent-name"]/text()')
                typeName = row.xpath('td[2]/a/text()')
                moveType = row.xpath('td[3]/@data-sort-value')
                description = row.xpath('td[7]/text()')
## NEXT we turn this into simple XML output


