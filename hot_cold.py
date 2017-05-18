import sys
import os
import time

def difficulty():
    while True:
        try:
            input_level = int(input("select difficulty level:  easy: 15 guesses, medium: 10 guesses and hard: 5 guesses "))
            if input_level in [5, 10, 15]:
                level = input_level
                break
        except ValueError:
            print('wrong input')
    return level
def guess_number(numbers, level):   
    while level > 0:
        guess = input("\nGuess a number: ")
        print(level)
        level -= 1
        guess_list = list(guess)

        for item in guess_list:
            for number in numbers:
                if item == number and guess_list.index(item) == numbers.index(number):
                    print('hot ', end='')
                elif item == number:
                    print('warm ', end = '')
            if item != number:
                print("cold ", end="")
            if numbers == guess_list:
                print("\nYou are correct!")
                break
            
            if level ==0:
                print("\nYou are lose!")
        play_again()

def play_again():
    play_again = input("\nDo you want to ply again ?: Y/N").lower()
    play = 0
    if play_again == 'y':
        os.system("clear")
    else:
        sys.exit()
            



def main():
    input_random = input("Enter a number: ")
    level = difficulty()
    while True:
        start_time = time.time()
        numbers = list(input_random)
        guess_number(numbers, level)
        end_time = time.time() - start_time
        print("time: ", int(end_time))
        play_again()
