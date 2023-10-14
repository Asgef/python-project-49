import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask_question():
    number = random.randint(1, 100)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def is_prime(number):
    if number < 4:
        return True
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1
    return True



