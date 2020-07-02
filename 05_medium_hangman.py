import random
import string

while True:
    game = input('Type "play" to play the game, "exit" to quit: ')
    if game == 'play':
        print('H A N G M A N')

        word_list = ['python', 'java', 'kotlin', 'javascript']
        tries = 8

        chosen_word = random.choice(word_list)
        chosen_word_list = list(chosen_word)
        chosen_word_set = set(chosen_word_list)

        guessing_word = list(len(chosen_word) * '-')
        typed_words = set()

        while tries > 0:
            print('')
            print(''.join(guessing_word))
            guess_letter = input('Input a letter: ')
            if guess_letter in typed_words:
                print('You already typed this letter')
            elif len(guess_letter) != 1:
                print('You should input a single letter')
            elif guess_letter not in string.ascii_lowercase:
                print('It is not an ASCII lowercase letter')
            elif guess_letter not in chosen_word_set:
                print('No such letter in the word')
                typed_words.add(guess_letter)
                tries -= 1
            if guess_letter in chosen_word_set:
                for i, j in enumerate(chosen_word_list):
                    if j == guess_letter:
                        guessing_word[i] = guess_letter
                typed_words.add(guess_letter)
            if tries == 0:
                print('You are hanged!')
            if ''.join(guessing_word) == chosen_word:
                print(f"You guessed the word {''.join(guessing_word)}!")
                print('You survived!')
                print('')
                break
    elif game == 'exit':
        break