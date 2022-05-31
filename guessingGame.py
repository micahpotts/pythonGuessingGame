#!/usr/bin/env python3

import random

def main():
    play = True

    while play:

        guessLimit = 0

        topOut = input("Pick a number.\n")
        topOut = int(topOut)

        rando = random.randint(1, topOut)

        print(
            "Guess a number between 1 and "
            + str(topOut)
            + " and I will tell you if it is too high or too low."
        )

        while guessLimit < topOut:
            guess = int(input())

            guessLimit = guessLimit + 1

            if rando > guess:
                print("You're too low, try again!")
            elif rando < guess:
                print("You're too high, try again!")
            else:
                print("You're the best! That's it!")
                again = input("Want to play again? (y/n)")
                if again == "y":
                    play == True
                    break
                else:
                    play == False
                    exit()
        else:
            print("You guessed " + str(topOut) + " times. Start again.")


if __name__ == "__main__":
    main()
