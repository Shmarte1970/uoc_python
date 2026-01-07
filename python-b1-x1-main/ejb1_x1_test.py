from ejb1_x1_main import *
from util_package.text_manager import TEXT
import pytest


def test_largest_word():
    assert find_largest_word(
        TEXT) == "nonpalindrome", "Check the function: find_largest_word"
    assert find_largest_word(
        "Hola este es mi libro de matemáticas") == "matemáticas", "Check the function: find_largest_word"
    assert find_largest_word(
        "Hola este es mi libro de matemáticas\nEn la actualidad prefiero un manual de refrigeradoras") == "refrigeradoras", "Check the function: find_largest_word"
    assert find_largest_word(
        "Hola este es mi libro de matemáticas\nEn la actualidad prefiero un manual de refrigeradoras\nPero por ahora tengo libros de Electroencefalografía disponibles  ") == "Electroencefalografía", "Check the function: find_largest_word"


def test_is_palindrome_word():
    assert is_palindrome_word(
        "aa") == True, "'aa' es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "a") == True, "'a' es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "Ababa") == True, "'Ababa' es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "abaaba") == True, "'abaaba' es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "ababa") == True, "'ababa' es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "Afromorfa") == True, "'Afromorfa' es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "Azuza") == True, "'Azuza' es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "abx") == False, "'abx' no es un palindrómo Check the function: is_palindrome_word"
    assert is_palindrome_word(
        "Miguel") == False, "'Miguel' no es un palindrómo Check the function: is_palindrome_word"


def test_count_palindrome_words():
    assert count_palindrome_words(
        TEXT) == 46, "Check the function: count_palindrome_words"
    assert count_palindrome_words(
        "civic, radar, level, rotor, kayak, madam, and refer.") == 7, "'Check the function: count_palindrome_words"
    assert count_palindrome_words(
        " Kayak; deified; Rotator; Repaper; deed; peep; wOw; nOOn; cIvic; racecar; lEvEl; mom; bird rib.") == 12, "'Check the function: count_palindrome_words"
    assert count_palindrome_words(
        "The is no palindrome\nAta; Aviva; Azuza; Apa; Afromorfa") == 5, "'Check the function: count_palindrome_words"
    assert count_palindrome_words("a r e r\nAta; Azuza; Apa; aa rr") == 9, "'Check the function: count_palindrome_words"


def test_find_size_largest_sentence():
    assert find_size_largest_sentence(
        TEXT, "a") == 51, "Check the function: find_size_largest_sentence"
    assert find_size_largest_sentence(
        TEXT, "next") == 44, "Check the function: find_size_largest_sentence"
    assert find_size_largest_sentence(
        TEXT, "one") == 44, "Check the function: find_size_largest_sentence"
    assert find_size_largest_sentence(
        TEXT, "paws") == 49, "Check the function: find_size_largest_sentence"
    assert find_size_largest_sentence(
        TEXT, "melon") == 19, "Check the function: find_size_largest_sentence"


def test_error_find_size_largest_sentence():
    with pytest.raises(
        ValueError
    ):
        find_size_largest_sentence(TEXT, "Texto No existe")
