"""Brain games cli module."""
import prompt


def welcome_user():
    """
    Welcomes and gets username and prompt that username.

    Returns
    -------
    name : str
        Username prompt.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    return name
