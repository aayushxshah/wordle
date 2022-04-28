import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END, messagebox
import random

words = list()
possibleGuesses = list()
answerList = list()
guessList = list()
global guessCounter
guessCounter = 0
colorList = list()

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
window_width = 400
window_height = 600
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
center_x = int(screenWidth/2 - window_width / 2)
center_y = int(screenHeight/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#center grid
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(6,weight=1)
window.grid_rowconfigure(0,weight=1)
window.grid_rowconfigure(8,weight=1)

#create entry box
entry = tk.Entry(width=10)
entry.grid(row = 7, column= 1, columnspan=5)


#pick answer
answerString = words[random.randint(0,len(words))]
print(answerString)

def clearText():
    #clear textbox
    entry.delete(0,END)

def newGuess(guessNumber, ansList, colorslist):

    guessl1 = ttk.Label(
        window,
        text = ansList[0],
        foreground=colorslist[0],
        font=("TkDefaultFont",50)
    ).grid(row=guessNumber,column=1)

    guessl2 = ttk.Label(
        window,
        text = ansList[1],
        foreground=colorslist[1],
        font=("TkDefaultFont",50)
    ).grid(row=guessNumber,column=2)

    guessl3 = ttk.Label(
        window,
        text = ansList[2],
        foreground=colorslist[2],
        font=("TkDefaultFont",50)
    ).grid(row=guessNumber,column=3)

    guessl4 = ttk.Label(
        window,
        text = ansList[3],
        foreground=colorslist[3],
        font=("TkDefaultFont",50)
    ).grid(row=guessNumber,column=4)

    guessl5 = ttk.Label(
        window,
        text = ansList[4],
        foreground=colorslist[4],
        font=("TkDefaultFont",50)
    ).grid(row=guessNumber,column=5)

def returnClick (event):

    global guessCounter

    #add each character as item in list
    for letter in answerString:
        answerList.append(letter)

    #input guess and make lowercase
    global entry
    guess = entry.get()
    guess = guess.lower()

    clearText()

    #check for length of guess
    if len(guess) > 5:
        messagebox.showinfo("Wordle Unlimited","Word too long.")
        print("Word too long.")
        return None

    elif len(guess) < 5:
        messagebox.showinfo("Wordle Unlimited","Word too short.")
        print("Word too short.")
        return None

    #check if it is an acceptable answer
    elif guess not in possibleGuesses and guess not in words:
        messagebox.showinfo("Wordle Unlimited","Word not in list.")
        print("Word not in list.")
        return None
        

    #if all conditions met add to guessCounter   
    else: guessCounter += 1

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
            colorList[i1] = "#b0b0b0"
        if g == a:
            colorList[i1] = "#286b24"
        elif g in answerList:
            colorList[i1] = "#c9be59"
        
        i1 += 1
    
    #newGuess(guessCounter,guessList)
    newGuess(guessCounter,guessList,colorList)

    #reset counter 2
    i2 = 0
    
    #check if user won
    if guessList == answerList:
        messagebox.showinfo("Wordle Unlimited","You Win!!")
        quit()
    
    #check if user lost
    if guessCounter == 6:
        messagebox.showinfo("Wordle Unlimited","You Lose!!")
        quit()


window.bind('<Return>', returnClick)
window.mainloop()