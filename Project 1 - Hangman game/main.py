
import random

import os

from graphic import logo
from graphic import stages
from words import word_list

print(logo)

chosen_word = random.choice(word_list)


display = []                                        # DISPLAY list variable
# empty display formation ----------------------
for letter in chosen_word:
    letter = "_"
    display.append(letter)
print(display)  

# main game repeat until lives 0 ---------------
lives = 6
end_of_game = False
guess_sort = []

while not end_of_game:
    print("------------------------------------------------------------------------------------")
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    if guess not in guess_sort:
        if guess in chosen_word:                    # TIP CORRECT
            count = 0
            guess_sort.append(guess)
            for letter in chosen_word:
                if letter == guess:
                    display[count] = letter
                    count += 1
                else:
                    count += 1
            print(f"You guessed a letter:{guess}\n:{display}")
            print(stages[lives])

            if "_" not in display:
                end_of_game = True
                print("You win")

        elif guess not in chosen_word and lives > 0:  # TIP NOT CORRECT
            guess_sort.append(guess)
            lives -= 1
            print(f"You guessed {guess}, that is not in the word. Remaining: {lives} lives\n{display}")
            print(stages[lives])
            if lives == 0:
                print(f"Correct word was:{chosen_word}")
                print("You lose")
                break
    else:
        print("You already tried this letter before")
        print(display)
        print(stages[lives])

