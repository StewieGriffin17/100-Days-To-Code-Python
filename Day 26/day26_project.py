# This program converts a user-input word into its NATO phonetic alphabet equivalent.
# For example, input "CAT" -> output ["Charlie", "Alfa", "Tango"].

import pandas

dataFrame = pandas.read_csv('./nato_phonetic_alphabet.csv')

alpha_dict = {row.letter: row.code for (index, row) in dataFrame.iterrows()}

user_input = input("Enter a word: ").upper()

output_list = [alpha_dict[letter] for letter in user_input]

print(output_list)
