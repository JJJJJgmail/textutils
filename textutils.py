"""A tiny collection of text helper functions."""


def reverse_words(text):
    """Reverse the order of words in a string.

    >>> reverse_words("hello world")
    'world hello'
    """
    return " ".join(reversed(text.split()))
