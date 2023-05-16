import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        print("\nGuess the word:")
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        guess = input("\nEnter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Wrong guess! Tries remaining:", tries)
        
        if set(word) == set(guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

    if tries == 0:
        print("\nSorry, you lost. The word was:", word)

play_game()
