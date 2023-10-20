import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

EVAN_MIN_LIMIT = 1
EVAN_MAX_LIMIT = 100


def get_question_answer():
    num = random.randint(EVAN_MIN_LIMIT, EVAN_MAX_LIMIT)
    answer = 'yes' if is_even(num) else 'no'
    return num, answer


def is_even(number):
    return number % 2 == 0
