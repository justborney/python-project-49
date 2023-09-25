"""Brain games cli module."""
import prompt


def welcome_user():
    """Get an user's name and promt that username."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
