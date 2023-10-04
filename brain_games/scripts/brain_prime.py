#!/usr/bin/env python3

from brain_games.games.common_logic import game_main
from brain_games.games.brain_game_even import (
    request_response_even, ask_question_even
)
from brain_games.games.brain_game_prime import (
    show_rules, process_data_prime
)


def main():
    return game_main(
        show_rules, ask_question_even,
        request_response_even, process_data_prime
    )


if __name__ == '__main__':
    main()
