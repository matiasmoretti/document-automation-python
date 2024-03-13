""""
Program: words_counter.py
Programmer: Matias Moretti
This is a word counter for the first assignmento of python
"""

REPLACE_NO_SPACE = ['.',',','"','!','?',':']
REPLACE_WITH_SPACE = ['--']

originFile = open(".\Assignment1\sample.txt","r")
text = originFile.read()
originFile.close()

for c in REPLACE_NO_SPACE:
    text = text.replace(c,"")

for c in REPLACE_WITH_SPACE:
    text = text.replace(c," ")

splitedText = text.upper().split()

wordsCounter = {}

for word in splitedText:
    wordsCounter[word] = splitedText.count(word)  

dic_desc_sorted = dict(sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True))    

reportFile = open(".\Assignment1\\report.txt","w")
reportFile.write("WORDS".ljust(20)+" | "+"FREQUENCY\n")
reportFile.write("".rjust(32,"=")+"\n")

for keyValue in dic_desc_sorted.keys():
    reportFile.write(keyValue.ljust(20) + " | " + str(dic_desc_sorted[keyValue]).rjust(9) + "\n")

reportFile.write("".rjust(32,"=")+"\n")

reportFile.write("TOTAL WORDS".rjust(20) + " | " + str(len(splitedText)).rjust(9)+"\n")
reportFile.write("TOTAL UNIQUE WORDS".rjust(20) + " | " + str(len(dic_desc_sorted)).rjust(9))

reportFile.close