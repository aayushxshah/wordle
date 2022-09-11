import re

wordsFile = open("wordle-answers-alphabetical.txt","r")
wordsContent = wordsFile.read()
words = wordsContent.split("\n")
wordsFile.close


greenletters = input("input green letters with * as place holder: ")
greenregex = greenletters.replace('*','.')

yellowletters = input("input yellow letters: ")

grayletters = input("input gray letters: ")

for word in words:
    if re.search(greenregex,word) != None:
        
        for yletter in yellowletters:
            if yletter in word:
                
                for gletter in grayletters:
                    if gletter not in word:
                        print(word)
