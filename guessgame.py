
import random

word_list = ["apple", "banana", "cherry", "orange", "kiwi", "grape", "watermelon","strawberry","guava","mango"]
random_word = random.choice(word_list)
# Choose a random index to remove a letter from the word

index_to_remove = random.randint(0, len(random_word)-1)

# Create the word with a blank space at the chosen index
display_word = random_word[:index_to_remove] + "_" + random_word[index_to_remove+1:]

print("Guess the missing letter in the word. You have 5 attempts.\n")
print("Word: " + display_word)

guesses_left = 5
guessed_letters = []

while "_" in display_word and guesses_left > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess == random_word[index_to_remove]:
        print("Correct!")
        display_word = display_word[:index_to_remove] + guess + display_word[index_to_remove+1:]
    else:
        guesses_left -= 1
        print("Wrong! You have", guesses_left, "guesses left.")

    print("Word: " + display_word)

if "_" not in display_word:
    print("Congratulations, you guessed the word!")
else:
    print("Sorry, you're out of guesses. The word was", random_word + ".")
