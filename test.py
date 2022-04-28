import tkinter as tk
import tkinter.ttk as ttk
import random

words = list()
possibleGuesses = list()
answerList = list()
guessList = list()
global guessCounter
guessCounter = 0

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
window.title("Wordle 2.0")

#window size and placement
window_width = 400
window_height = 600
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
center_x = int(screenWidth/2 - window_width / 2)
center_y = int(screenHeight/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#create entry box
entry = tk.Entry(width=10)
entry.grid(row = 6, column= 0, columnspan=5)


#pick answer
answerString = words[random.randint(0,len(words))]
print(answerString)

def newGuess(guessNumber, ansList):

    

    guessl0 = ttk.Label(
        window,
        text = ansList[0],
        foreground="white"
    ).grid(row=guessNumber,column=0)

    guessl1 = ttk.Label(
        window,
        text = ansList[1],
        foreground="white"
    ).grid(row=guessNumber,column=1)

    guessl2 = ttk.Label(
        window,
        text = ansList[2],
        foreground="white"
    ).grid(row=guessNumber,column=2)

    guessl3 = ttk.Label(
        window,
        text = ansList[3],
        foreground="white"
    ).grid(row=guessNumber,column=3)

    guessl4 = ttk.Label(
        window,
        text = ansList[4],
        foreground="white"
    ).grid(row=guessNumber,column=4)

def returnClick (event):
    print("return")
    #add each character as item in list
    for letter in answerString:
        answerList.append(letter)

        #input guess and make lowercase
    global entry
    guess = entry.get()
    guess = guess.lower()

    #check for length of guess
    if len(guess) > 5:
        print("Word too long.")
        

    elif len(guess) < 5:
        print("Word too short.")
        

    #check if it is an acceptable answer
    elif guess not in possibleGuesses and guess not in words:
        print("Word not in list.")
        

    #if all conditions met add to guessCounter   
    else: guessCounter += 1

    #clear list
    guessList = []

    #make list with each character as item of guess
    for letter in guess:
        guessList.append(letter)

    #reset counter 1
    i1 = 0

    #newGuess(guessCounter,guessList)
    newGuess(0,guessList)

    #check to see what color letter is assigned
    for g in guessList:

        a = answerList[i1]

        if g != a:
            guessList[i1] = " - gray"
        if g == a:
            guessList[i1] = " - green"
        elif g in answerList:
            guessList[i1] = " - yellow"
        
        i1 += 1

    #reset counter 2
    i2 = 0
    
    #print results
    for char in guess:
        print(str(char)+guessList[i2])
        i2 += 1

    #check if user won
    correctGuessList = [" - green"," - green"," - green"," - green"," - green",]
    if guessList == correctGuessList:
        print("You Win!")


window.bind('<Return>', returnClick)
window.mainloop()

##########################################