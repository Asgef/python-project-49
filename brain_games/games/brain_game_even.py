import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_question():
    num = random.randint(1, 100)
    if is_even(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
