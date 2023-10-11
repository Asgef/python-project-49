from brain_games.games.brain_game_even import ask_question

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def process_data(num):
    if num < 4:
        return True
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return False
        i += 1
    return True


question, correct_answer = ask_question(process_data)
