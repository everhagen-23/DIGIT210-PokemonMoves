import bs4
from lxml import etree
from lxml import html
import os
import pandas as pd

collPath = "data"
# Create the root XML element for the output
root = etree.Element("moveSet")

move_data = []


for file in os.listdir(collPath):
    if file.endswith(".html"):
        filepath = f"{collPath}/{file}"
        gen, extension = os.path.splitext(file)
        print(gen)
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
        ## NEXT we turn this into simple XML output:
                if moveName:
                    moveEl = etree.SubElement(root, "move")
                    etree.SubElement(moveEl, "gen").text = gen
                    # ebb just grab this from the filename so each move is associated with its generation.
                    etree.SubElement(moveEl, "name").text = moveName[0].strip() if moveName else ''
                    # ebb: for these elements, the output was in list form with []'s, so strip() literally
                    # *deforms* the list and makes it a string.
                    etree.SubElement(moveEl, "category").text = typeName[0].strip() if typeName else ''
                    etree.SubElement(moveEl, "type").text = moveType[0].strip() if moveType else ''
                    etree.SubElement(moveEl, "description").text = description[0].strip() if description else ''

                    ## Can we just make some nice dataframes from this, too, and output a TSV?
                    ## WE can collect the same data in a moveData list. We'll start an empty one up above th for loop
                    move_data.append({
                        "gen": gen,
                        "name": moveName[0].strip() if moveName else '',
                        "category": typeName[0].strip() if typeName else '',
                        "type": moveType[0].strip() if moveType else '',
                        "description": description[0].strip() if description else ''
                    })

# Serialize the XML to a string or save to file
xml_output = etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True)

# Save to XML file
with open("pokemonMoves.xml", "wb") as f:
    f.write(xml_output)

# Save dataframes to TSV
df = pd.DataFrame(move_data)
df.to_csv("moves_output.tsv", sep="\t", index=False)
