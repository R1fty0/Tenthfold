import random

numbers = []
SLOTS = 4


class GameManager:
    def __init__(self, SLOTS, TIMER):
        """ Handles Game Mechanics. """
        self.SLOTS = SLOTS
        self.TIMER = TIMER

    def generate_numbers(self, numbersList):
        """ Generates numbers depending on the number of slots."""
        currentSlot = 0
        while currentSlot != self.SLOTS:
            number = random.randrange(1, 9)
            numbersList.append(number)
            currentSlot += 1
            print(number)

    def countdown_timer(self):
        """ Game's internal clock - the game ends after the timer runs out if the user does not input an answer."""
        pass


def user_input():
    """ Handles User Input. """
    slot = input("Select the slot you would like to access!: ")
    operation = input("What is the operation you would like to access!: ")


def game():
    """ Core Game Loop - all game logic occurs here. """

    GM = GameManager(4)  # Creates an instance of the Game Manager class

    GM.generate_numbers(numbers)  # Generates random numbers for each slot

    running = True

    while running:
        pass


if __name__ == "__main__":
    game()