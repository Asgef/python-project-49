from brain_games import cli


def game_main(show_rules, issue_a_question, request_response, process_data):
    user_name = cli.welcome_user()
    print(show_rules)
    count = 0
    number_repetitions = 3
    while count < number_repetitions:
        question = issue_a_question()
        answer = request_response()
        processed_response = process_data(question, answer)
        if processed_response[0]:
            print('Correct!')
            count += 1
        else:
            was = processed_response[1]
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer {was}."
                f"\nLet's try again, {user_name}!!!"
            )
            return 0
        print(f'Congratulations, {user_name}!')

