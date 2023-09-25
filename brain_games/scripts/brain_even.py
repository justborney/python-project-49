#!/usr/bin/env python
"""Is even game module."""

from random import randint
import prompt

from brain_games.cli import welcome_user


def is_even(number):
    """
    Check number is even or not

    :param number: number
    :returns: True or False based on even
    """
    """Check number is even."""
    return True if number % 2 == 0 else False


def init_game(min, max):
    number = randint(min, max)
    question = '{}'.format(number)

    result = 'yes' if is_even(number) else 'no'

    return question, result


def even_game():
    start_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    wrong_answer = '"{}" is wrong answer ;(. Correct answer was "{}".\nLet\'s try again, {}!'
    correct_answer = 'Correct!'
    victory_message = 'Congratulations, {}!'
    win_condition = 3
    min_number = 1
    max_number = 100

    username = welcome_user()
    print(start_message)
    count = 0

    while count < win_condition:
        question, result = init_game(min_number, max_number)
        print('Question: {}'.format(question))
        user_guess = prompt.string('Your answer: ')

        user_result = str(result) == user_guess.lower()

        if not user_result:
            print(wrong_answer.format(user_guess.lower(), result, username))
            break

        print(correct_answer)

        if count == win_condition - 1:
            print(victory_message.format(username))

        count += 1


def main():
    even_game()


if __name__ == '__main__':
    main()
