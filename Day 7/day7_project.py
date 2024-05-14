# Today, there is no new concept. Today I will use the previous learnt concepts to create a replica of popular "hangman" game.
import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['abruptly', 'absurd', 'awkward', 'bagpipes', 'bandwagon', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'bookworm', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buzzard', 'buzzing', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypto', 'cycle', 'dizzying', 'duplex', 'faking', 'fishhook', 'fixable', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'funny', 'galaxy', 'glowworm', 'icebox', 'injury', 'jackpot', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo',  'keyhole', 'khaki', 'kilobyte', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'micro', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'witchcraft', 'wizard', 'youthful', 'yummy', 'zipper', 'zodiac']

chosen_word = word_list[random.randint(0, len(word_list)-1)]
blank_word = []
lives = 6
# Creating blank list
for _ in range(len(chosen_word)):
    blank_word.append("_")
blanks = blank_word.count("_")

# User interface
print("WELLCOME TO HANGMAN!!!")
print("press 1 to play, press any other number to see the rules.")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(blank_word)

    # Running a loop until each blank space is replaced with correct letter
    while not blanks == 0:
        guess = input("Guess a letter : ").lower()

        # Replacing the blank space with user input if the letter exists in the word
        if guess in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    blank_word[position] = guess
                    blanks -= 1
            print(blank_word)
            if blanks == 0:
                print("You win!!!")

        # Decreasing a life for each wrong guess and printing out the stage
        elif guess not in chosen_word:
            print(f"{guess} is not in the word. Try again.")
            print(stages[lives])
            lives -= 1
            print(f"REMAINING LIVES : {lives} \n")
            if lives == 0:
                print(stages[lives])
                print("YOU LOSE!!!")
                exit()  # Exit the program if the user run out of lives
else:
    print("Hangman is a simple game. Here are the rules for this game: \n1. The game starts with a hidden word ,represented by blanks.\n2. Try guessing the letters in the word.\n3. If the guessed letter is in the word, it is revealed in the correct position(s).\n4. If the guessed letter is not in the word, you lose one life.\n5. You starts with 6 lives, and each incorrect guess costs one life.\n6. Guess the word before you run out of lives.")
