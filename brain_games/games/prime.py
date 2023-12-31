import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

PRIME_MIN_BOUND = 1
PRIME_Max_BOUND = 100


def get_question_answer():
    number = random.randint(PRIME_MIN_BOUND, PRIME_Max_BOUND)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def is_prime(number):
    if number < 4:
        return True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True
