import pytest
from ej3c2 import calculate_reading_time


# Prueba para la aplicación de la función lambda con map
def test_books_with_reading_time():
    # Lista de libros de prueba
    books = [
        {"title": "Book Title 1", "author": "David Perry", "pages": 879},
        {"title": "Book Title 2", "author": "Jacqueline Johnson", "pages": 657},
        {"title": "Book Title 97", "author": "Linda Contreras", "pages": 194},
    ]
    books_with_reading_time = list(
        map(lambda book: {**book, "reading_time": calculate_reading_time(book)}, books)
    )
    assert all(
        "reading_time" in book for book in books_with_reading_time
    ), "Not all books have a 'reading_time' field."
    assert books_with_reading_time[0]["reading_time"] == round(
        (879 * 250) / 200
    ), "The reading time for the first book is incorrect."
    assert books_with_reading_time[1]["reading_time"] == round(
        (657 * 250) / 200
    ), "The reading time for the second book is incorrect."
    assert books_with_reading_time[2]["reading_time"] == round(
        (194 * 250) / 200
    ), "The reading time for the third book is incorrect."
