#!/usr/bin/env python3

from brain_games.games.common_logic import game_main
from brain_games.games.brain_game_calc import request_response_calc
from brain_games.games.brain_game_gcd import (
    show_rules, ask_question_gcd, process_data_gcd
)


def main():
    return game_main(
        show_rules, ask_question_gcd,
        request_response_calc, process_data_gcd
    )


if __name__ == '__main__':
    main()
