import random
import time
import os

# Dictionary containing secret words and their corresponding answers
secret_words = {
    "What tastes better than it smells? ": "TONGUE",
    "What building has the most stories? ": "LIBRARY",
    "What has a bottom at the top? ": "LEG",
    "What has four wheels and flies? ": "GARBAGE TRUCK",
    "What can you put in a bucket to make it weigh less? ": "HOLE",
    "What starts with T, ends with T, and has T in it? ": "TEAPOT",
    "Where is the only place where today comes before yesterday? ": "DICTIONARY",
    "What goes all around the world but stays in a corner? ": "STAMP",
    "What type of cheese is made backward? ": "EDAM",
    "What kind of ship has two mates but no captain? ": "RELATIONSHIP",
    "Who has married many people but has never been married himself? ": "PRIEST",
    "If you throw a blue stone into the Red Sea, what will it become? ": "WET",
    "Which word in the dictionary is spelled incorrectly? ": "INCORRECTLY",
    "What has three feet but cannot walk? ": "YARDSTICK",
    "What do you call a nose that's 12 inches long? ": "FOOT",
    "What has to be broken before you can use it? ": "EGG",
    "What gets shorter as it grows older? ": "CANDLE",
    "What can you catch but never throw? ": "COLD",
    "What runs around a whole yard without moving? ": "FENCE",
    "What five-letter word becomes shorter when you add two letters to it? ": "SHORT"
}

# Function to select a random question and its answer from the dictionary
def select_random_question():
    question, answer = random.choice(list(secret_words.items()))
    return question, answer

# Function to clear the terminal screen
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to play the quiz
def play_quiz():
    guess_count = 0
    correct_answers = 0


    # Main loop for the quiz
    while guess_count < 5:
        clear_terminal()  # Clear the terminal before each question
        question, answer = select_random_question()
        guess = input(question).upper()  # Get user input and convert to uppercase

        print("Your guess was " + guess + "...")
        time.sleep(1.3)

        # Check if the guess is correct
        if guess == answer:
            print("Your guess is correct! You are clever!")
            correct_answers += 1
            print('Correct answers: ' + str(correct_answers))
        else:
            print("Your guess is wrong! Try again.")
            guess_count += 1
            print("Guess count: " + str(guess_count))

        # Check if the user wants to continue or exit
        if guess_count < 5:
            continue_quiz = input("Press 1 to continue the quiz, or 2 to exit: ")
            if continue_quiz != '1':
                break

    # End of the quiz
    print("\nGame over! You answered " + str(correct_answers) + " questions correctly.")

    # Print all the secret words and their answers
    print("\nHere are all the secret words:")
    for question, answer in secret_words.items():
        print(question + "(Answer: " + answer + ")")

# Entry point of the program
if __name__ == "__main__":
    play_quiz()