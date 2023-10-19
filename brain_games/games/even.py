import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_VALUE = 1
MAX_VALUE = 100


def get_question_answer():
    num = random.randint(MIN_VALUE, MAX_VALUE)
    if is_even(num):
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer


def is_even(number):
    return number % 2 == 0
