#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
df1 = pandas.DataFrame(df)
df2 = {row.letter: row.code for (index, row) in df1.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("enter name").upper()
user_input1 = list(user_input)
user_answer = [df2[i] for i in user_input1]
print(user_answer)

