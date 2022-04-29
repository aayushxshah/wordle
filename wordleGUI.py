from string import ascii_lowercase
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END, messagebox
import random

words = list()
possibleGuesses = list()
answerList = list()
guessList = list()
guessCounter = 0
colorList = list()
rowNum = 1
columnNum = 7
letterColor = dict()

#create list of possible answers
wordsFile = open("wordle-answers-alphabetical.txt","r")
wordsContent = wordsFile.read()
words = wordsContent.split("\n")
wordsFile.close

#create list of possible guesses
possibleGuessesFile = open("wordle-allowed-guesses.txt","r")
possibleGuessesContent = possibleGuessesFile.read()
possibleGuesses = possibleGuessesContent.split("\n")
possibleGuessesFile.close

#initialize window
window = tk.Tk()
window.title("Wordle Unlimited")

#window size and placement
window_width = 600
window_height = 600
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
center_x = int(screenWidth/2 - window_width / 2)
center_y = int(screenHeight/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#window.configure(bg = 'gray')

#center grid
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(6,weight=1)
window.grid_columnconfigure(12,weight=1)
window.grid_rowconfigure(0,weight=1)
window.grid_rowconfigure(8,weight=1)

#create entry box
entry = tk.Entry(
    width=10,
    font=("Courier",50),
    justify='center'
    )
entry.grid(row = 7, column= 1, columnspan=5)

#pick answer
answerString = words[random.randint(0,len(words))]

for letter in ascii_lowercase:
    letterColor[letter] = 'white'

#add each character as item in list
for letter in answerString:
    answerList.append(letter)

#clear text in entrybox
def clearText():
    #clear textbox
    entry.delete(0,END)

#makes new row of label for each guess
def newGuess(guessNumber, ansList, colorslist):

    guessl1 = ttk.Label(
        window,
        background = 'gray',
        text = ansList[0],
        foreground=colorslist[0],
        font=("Courier",75)
    ).grid(row=guessNumber,column=1)

    guessl2 = ttk.Label(
        window,
        text = ansList[1],
        foreground=colorslist[1],
        font=("Courier",75)
    ).grid(row=guessNumber,column=2)

    guessl3 = ttk.Label(
        window,
        text = ansList[2],
        foreground=colorslist[2],
        font=("Courier",75)
    ).grid(row=guessNumber,column=3)

    guessl4 = ttk.Label(
        window,
        text = ansList[3],
        foreground=colorslist[3],
        font=("Courier",75)
    ).grid(row=guessNumber,column=4)

    guessl5 = ttk.Label(
        window,
        text = ansList[4],
        foreground=colorslist[4],
        font=("Courier",75)
    ).grid(row=guessNumber,column=5)

#ran when return in pressed
def returnClick (event):

    #makes variables accessible inside function
    global guessCounter
    global answerList
    global letterColor
    global rowNum
    global columnNum

    #input guess and make lowercase
    global entry
    guess = entry.get()
    guess = guess.lower()

    #check for length of guess
    if len(guess) > 5:
        messagebox.showinfo("Wordle Unlimited","Word too long.")
        entry.focus_set()
        return None

    elif len(guess) < 5:
        messagebox.showinfo("Wordle Unlimited","Word too short.")
        entry.focus_set()
        return None

    #check if it is an acceptable answer
    elif guess not in possibleGuesses and guess not in words:
        messagebox.showinfo("Wordle Unlimited","Word not in list.")
        entry.focus_set()
        return None
        

    #if all conditions met add to guessCounter   
    else: guessCounter += 1

    #clears entry box text
    clearText()

    #clear list
    guessList = []
    colorList = [None,None,None,None,None]

    #make list with each character as item of guess
    for letter in guess:
        guessList.append(letter)
    
    #reset counter 1
    i1 = 0

    #check to see what color letter is assigned
    for g in guessList:

        a = answerList[i1]

        if g != a:
            colorList[i1] = "#8d9092"
        if g == a:
            colorList[i1] = "#286b24"
        elif g in answerList:
            colorList[i1] = "#c9be59"
        
        i1 += 1
    
    #update colors in letterColor
    for letter in guessList:
        if letter in letterColor:
            letterColor[letter] = colorList[guessList.index(letter)]
    
    #reset row and column counter
    rowNum = 1
    columnNum = 7

    #clear letters
    for letter in ascii_lowercase:
        newLetter(' ','white')

    #reset row and column counter
    rowNum = 1
    columnNum = 7

    #create new letters with update colors
    for letter in ascii_lowercase:
        newLetter(letter,letterColor[letter])
        

    
    #creates new row with guess
    newGuess(guessCounter,guessList,colorList)

    #reset counter 2
    i2 = 0
    
    #check if user won
    if guessList == answerList:
        messagebox.showinfo("Wordle Unlimited","You Win!!")
        return None
    
    #check if user lost
    if guessCounter == 6:
        messagebox.showinfo("Wordle Unlimited","You Lose!!")
        return None

#makes label for letter
def newLetter(letter,color):

    global rowNum
    global columnNum

    #moves to next row at end of row
    if columnNum == 12:
        columnNum = 7
        rowNum += 1

    #makes label
    letterLabel = ttk.Label(
        window,
        text = letter,
        font=("Courier",25)
    )
    letterLabel.grid(row=rowNum,column=columnNum)

    #uses defualt color for uncolored letters
    if color == 'white':
        pass
    else:
        letterLabel.configure(foreground=letterColor[letter])
    
    #next column
    columnNum += 1

#placeholder rows
blankans = [" "," "," "," "," "]
blankcolor = ["white","white","white","white","white"]

newGuess(1,blankans,blankcolor)
newGuess(2,blankans,blankcolor)
newGuess(3,blankans,blankcolor)
newGuess(4,blankans,blankcolor)
newGuess(5,blankans,blankcolor)
newGuess(6,blankans,blankcolor)

#makes letters at startup
for letter in ascii_lowercase:
    newLetter(letter,letterColor[letter])

entry.focus_set()
window.bind('<Return>', returnClick)
window.mainloop()