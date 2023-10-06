#!/usr/bin/env python3

from brain_games.games.common_logic import game_main
from brain_games.games.brain_game_calc import (
    show_rules, ask_question_calc, process_data_calc, request_response_calc
)


def main():
    return game_main(
        show_rules, ask_question_calc,
        request_response_calc, process_data_calc
    )


if __name__ == '__main__':
    main()
