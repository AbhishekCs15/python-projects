import random

#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
a=random.choice(word_list)
b=list(a)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("guess a letter ").lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in b:
    if i==guess:
        print("true")
    else:
        print("False")



#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
display=[]
#For each letter in the chosen_word, add a "_" to 'display'.
for i in chosen_word:
    display.append("-")

#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
print(display)
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
for postition in range(len(chosen_word)):



#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    letter=chosen_word[postition]
    if letter == guess:
       display[postition]=letter
    
        
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)















