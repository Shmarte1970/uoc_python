from ej6c2 import read_txt_file, words_counter
import pathlib, os


def test_read_txt_file():
    # Checking how pytest was called lo locate the file
    launch_path = pathlib.Path.cwd()
    path = "files" + os.sep + "ej6c2_data_engineer.txt"
    if str(launch_path).split(os.sep)[-1].startswith("python-b1"):
        path = "6c" + os.sep + path

    expected_output_25_characters = "What is a data engineer a"
    assert (
        read_txt_file(path)[:25] == expected_output_25_characters
    ), "The text of the file does not match, it should start with 'What is a data engineer a'"

    expected_output_last_25_characters = "iable, and ready for use."
    assert (
        read_txt_file(path)[-25:] == expected_output_last_25_characters
    ), "The text of the does not match, it should end with 'iable, and ready for use.'"


def test_words_counter():
    text = "The quick brown fox jumps over the lazy dog."
    word = "the"
    expected_output = 2
    assert (
        words_counter(text, word) == expected_output
    ), "The counter number does not match, it should be 2 for the word 'the'"

    text = "data has become one of the most valuable assets for companies."
    word = "foo"
    expected_output = 0
    assert (
        words_counter(text, word) == expected_output
    ), "The counter number does not match, it should be 0 for the word 'foo'"

    text = "The quick brown fox jumps over the lazy dog."
    word = "FOX"
    expected_output = 1
    assert (
        words_counter(text, word) == expected_output
    ), "The counter number does not match, it should be 1 for the word 'FOX'"
