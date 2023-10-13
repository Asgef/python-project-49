from brain_games import cli
from brain_games.games import (
    brain_game_even, brain_game_calc, brain_game_gcd,
    brain_game_progression, brain_game_prime
)
import prompt

NUM_ROUNDS = 3


def game_main(game):
    user_name = cli.welcome_user()
    print(game.RULE)
    count = 0
    while count < NUM_ROUNDS:
        question, correct_answer = game.ask_question(game.process_data)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"\nLet's try again, {user_name}!!!"
            )
            return 0
    print(f'Congratulations, {user_name}!')


even = brain_game_even
calc = brain_game_calc
gcd = brain_game_gcd
progression = brain_game_progression
prime = brain_game_prime
