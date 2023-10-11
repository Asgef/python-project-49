#!/usr/bin/env python3

from brain_games.games import brain_game_calc
from brain_games.engine import game_main


def main():
    return game_main(brain_game_calc)


if __name__ == '__main__':
    main()
