from .brain_game_even import invert_answer

show_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 4:
        return True
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return False
        i += 1
    return True


def process_data_prime(question, answer):
    number_prime = is_prime(question)
    if number_prime and answer == 'yes':
        return True, 0,
    elif number_prime is False and answer == 'no':
        return True, 0,
    else:
        return False, invert_answer(answer)
