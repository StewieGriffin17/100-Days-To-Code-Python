# This program converts a user-input word into its NATO phonetic alphabet equivalent.
# For example, input "CAT" -> output ["Charlie", "Alfa", "Tango"].
# Updated version of previous project with error handling

import pandas

dataFrame = pandas.read_csv('./nato_phonetic_alphabet.csv')

alpha_dict = {row.letter: row.code for (index, row) in dataFrame.iterrows()}

def generate():
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [alpha_dict[letter] for letter in user_input]
    except KeyError:
        print("sorry, Only letters in the alphabet please.")
        generate()
    else:
        print(output_list)

generate()
