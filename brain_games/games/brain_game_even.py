import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_question(process_data_func):
    number = random.randint(1, 100)
    if process_data_func(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number, correct_answer


def process_data(number):
    if number % 2 == 0:
        return True
    else:
        return False
