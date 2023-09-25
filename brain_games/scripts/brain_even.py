#!/uer/bin/env python3

from .. import cli
import prompt
import random


def show_rules():
    print('Answer "yes" if the is even, otherwise answer "no".')


def ask_question():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    return number


def request_response():
    return prompt.string('Your answer: ')


def process_data(question, answer):
    if question % 2 == 0 and answer == 'yes':
        return True
    elif question % 2 != 0 and answer == 'no':
        return True
    else:
        return False


def invert_answer(answer):
    if answer == 'yes':
        return 'no'
    elif answer == 'no':
        return 'yes'
    else:
        return "'yes' or 'no'"


def main():
    user_name = cli.welcome_user()
    show_rules()
    count = 0
    number_repetitions = 3
    while count < number_repetitions:
        question = ask_question()
        answer = request_response()
        if process_data(question, answer):
            print('Correct!')
            count += 1
        else:
            return print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer '{invert_answer(answer)}'"
                f"\nLet's try again, {user_name}!!!"
            )
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
