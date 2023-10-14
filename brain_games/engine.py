from brain_games import cli
import prompt

NUM_ROUNDS = 3


def game_main(game):
    user_name = cli.welcome_user()
    print(game.RULE)
    count = 0
    while count < NUM_ROUNDS:
        question, correct_answer = game.ask_question()
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
