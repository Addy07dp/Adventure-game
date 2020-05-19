import time
import random


def print_pause(msg):
    print(msg)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        if response in options:
            return(response)


def play_again(creature, weapon):
    play_again = valid_input("Would you like to play "
                             "again? (y/n)\n", ["y", "n"])
    if play_again == 'y':
        intro(creature, weapon)
    else:
        print("Thanks for playing! See you next time.")


def weapons(creature, weapon):
    if len(weapon) == 0:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
        fight = valid_input("Would you like to (1) fight or "
                            "(2) run away?\n", ["1", "2"])
        if fight == '1':
            print_pause("You do your best...")
            print_pause("but your dagger is no match for "
                        "the " + creature + ".")
            print_pause("You have been defeated!")
            play_again(creature, weapon)
        else:
            print_pause("You run back into the field. Luckily,"
                        " you don't seem to have been followed.\n")
            field(creature, weapon)
    else:
        fight = valid_input("Would you like to (1) fight "
                            "or (2) run away?\n", ["1", "2"])
        if fight == '1':
            print_pause("As the " + creature + " moves to "
                        "attack, you unsheath your new weapon.")
            print_pause("The " + weapon[0] + " shines brightly "
                        "in your hand as you brace yourself for the attack.")
            print_pause("But the " + creature + " takes one "
                        "look at your shiny new toy and runs away!")
            print_pause("You have rid the town from "
                        "the " + creature + ". You are victorious!")
            weapon.pop()
            play_again(creature, weapon)
        else:
            print_pause("You run back into the field."
                        " Luckily, you don't seem to have been followed.\n")
            field(creature, weapon)


def house(creature, weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + creature + ".")
    print_pause("Eep! This is the " + creature + "'s house!")
    print_pause("The " + creature + " attacks you!")
    weapons(creature, weapon)


def cave(creature, weapon):
    print_pause("You peer cautiously into the cave.")
    if len(weapon) == 0:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        weapon.append(random.choice(["sword of ogoroth", "ring "
                                     "of fortune", "blade of zeus"]))
        print_pause("You have found the magical " + weapon[0] + "!")
        print_pause("You discard your silly old dagger "
                    "and take the " + weapon[0] + " with you.")
    else:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    field(creature, weapon)


def field(creature, weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2.)\n", ["1", "2"])
    if choice == '1':
        house(creature, weapon)
    else:
        cave(creature, weapon)


def intro(creature, weapon):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + creature + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")
    field(creature, weapon)


def play():
    creature = random.choice(["gorgons", "Wicked fairy",
                              "dragon", "troll", "Wicked pirate"])
    weapon = []
    intro(creature, weapon)


play()
