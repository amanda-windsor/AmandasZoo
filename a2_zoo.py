"""
CP1401 2021-2 Assignment 2
Simple Zoo Simulator
Student Name: Amanda Windsor
Date started: 11/10/2021

Pseudocode:
import random
make constant for LOW_LUCK_THRESHOLD
Make constant for MENU
make list for animals

Print Welcome Message
print animals
start counter for days, total_income
print menu message, MENU
get user_choice
    while user_choice is not q
        if user_choice is w
            add 1 to day counter
            generate random luck number
            print luck message
            if luck is in LOW_LUCK_THRESHOLD
                run unlucky_day function
            for each animal in animals
                run simulate_day function
                add daily_income to total_income
        else if user_choice is d
            run display_animals function
        else if user_choice is a
            get new_animal
            if new_animal is blank
                print Invalid Input message
            else if new_animal is already in animals
                print You already have new_animal message
            else if length of new_animal is greater than total_income
                print You can not afford new_animal message
            else add new_animal to animals
            calculate animal_cost
                deduct animal_cost from total_income
        else
            print Invalid choice message
    print menu message
    print MENU
print farewell message


definition display_animals
sort animals into alphabetical order
    if length of animals is 0
        print Oh no! You have no animals! message
    else for each animal in animals
        print animals
"""


import random

LOW_LUCK_THRESHOLD = 33
MENU = "(W)ait\n(D)isplay animals\n(A)dd new animal\n(Q)uit"
animals = ['Charmander', 'Squirtle', 'Bulbasaur']


def simulate_day(daily_income, luck, animal):
    """This function calculates daily income for each animal"""
    daily_income = 0
    daily_income += (luck / 100) * len(animal)
    print(f"{animal} earned {int(daily_income)}", end=', ')
    return int(daily_income)


def unlucky_day():
    """This function removes a random animal from the animal list"""
    random_animal = random.choice(animals)
    animals.remove(random_animal)
    print(f"Nooooooo! Your {random_animal.title()} escaped!")


def display_animals():
    """This function sorts animals into alphabetical order and then displays"""
    animals.sort()
    if len(animals) == 0:
        print("Oh no! You have no animals!")
    else:
        for animal in animals:
            print(animal.title(), end=", ")


def determine_day_string(days):
    """This function determines correct wording"""
    if days == 1:
        day_word = "day"
    else:
        day_word = "days"
    return day_word


def determine_animal_string():
    """This function determines correct wording"""
    if len(animals) == 1:
        animal_word = "animal"
    else:
        animal_word = "animals"
    return animal_word


def main():
    """Simple Zoo Simulator Program"""
    print("""Welcome to Amanda's Zoo!
Animals cost and generate income according to their name length (e.g., a Dog costs 3).
Each day, animals generate income based on luck. Sometimes they escape.
You can buy new animals with the income your Safari generates.
You start with these animals:""")
    display_animals()
    total_income = 0
    days = 0
    print(f"\nAfter {days} {determine_day_string(days)}, you have {len(animals)} {determine_animal_string()}"
          f" and your total income is {total_income}.")
    print(MENU)
    user_choice = input("Choose: ").lower()
    while user_choice != 'q':
        if user_choice == 'w':  # Simulate day and determine income based on lucky number.
            days += 1
            luck = random.randint(0, 100)
            print(f"Today's lucky number is {luck}.")
            if luck < LOW_LUCK_THRESHOLD:
                unlucky_day()
            for animal in animals:
                daily_income = simulate_day(total_income, luck, animal)
                total_income += daily_income
        elif user_choice == 'd':
            display_animals()
        elif user_choice == 'a':  # Add new animal to list with error checking.
            new_animal = (input("Animal name: ").title())
            if new_animal == "":
                print("Invalid Input")
            elif new_animal in animals:
                print(f"You already have {new_animal}.")
            elif len(new_animal) > total_income:
                print(f"You can not afford {new_animal}.")
            else:
                animals.append(new_animal)
                animal_cost = len(new_animal)
                total_income -= animal_cost
        else:
            print("Invalid choice.")
        print(f"\nAfter {days} {determine_day_string(days)}, you have {len(animals)} {determine_animal_string()} "
              f"and your total income is {total_income}.")
        print(MENU)
        user_choice = input("Choose: ").lower()
    print(f"""You finished with {len(animals)} {determine_animal_string()}.
After {days} {determine_day_string(days)}, you have {len(animals)} {determine_animal_string()} 
and your total income is {total_income}.""")


main()
