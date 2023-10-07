import random
from brain_games.games.brain_game_calc import request_response_calc
from brain_games.engine import game_main

RULE = 'Find the greatest common divisor of given numbers.'


def ask_question_gcd():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'Question: {number_1} {number_2}'
    print(question)
    return number_1, number_2,


def process_data_gcd(question, answer):
    a = question[0]
    b = question[1]
    while b:
        a, b = b, a % b
    gcd = a
    if gcd == answer:
        return True, gcd,
    else:
        return False, f'was {gcd}',


def game_gcd():
    return game_main(
        RULE, ask_question_gcd,
        request_response_calc, process_data_gcd
    )
