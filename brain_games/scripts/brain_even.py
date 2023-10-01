#!/usr/bin/env python3

from brain_games.games.common_logic import game_main
from brain_games.games.brain_game_even import show_rules, ask_question_even, process_data_even, request_response_even


def main():
    return game_main(show_rules, ask_question_even, request_response_even, process_data_even)


if __name__ == '__main__':
    main()

