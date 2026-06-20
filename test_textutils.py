"""Tests for textutils."""

from textutils import reverse_words


def test_reverse_words_basic():
    assert reverse_words("hello world") == "world hello"


def test_reverse_words_single_word():
    assert reverse_words("hello") == "hello"


def test_reverse_words_empty_string():
    assert reverse_words("") == ""


def test_reverse_words_collapses_extra_whitespace():
    assert reverse_words("  a   b  ") == "b a"
