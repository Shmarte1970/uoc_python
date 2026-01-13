from ej3c3 import generate_passwords


def test_generate_passwords_length():
    """
    Test para asegurar que la longitud de las contraseñas generadas es correcta.
    """
    password_length = 4
    passwords = generate_passwords(password_length)
    for password in passwords:
        assert len(password) == password_length, "The length of the generated passwords is incorrect."

def test_generate_passwords_count():
    """
    Test to verify the number of generated passwords.
    """
    password_length = 4
    expected_count = (2 + 2 + 2 + 2) ** password_length  # Cada grupo tiene 2 caracteres, repetido por la longitud de la contraseña
    passwords = generate_passwords(password_length)
    assert len(passwords) == expected_count, "The number of generated passwords is incorrect."

def test_generate_passwords_uniqueness():
    """
    Test to ensure that the generated passwords are unique.
    """
    password_length = 4
    passwords = generate_passwords(password_length)
    assert len(passwords) == len(set(passwords)), "The generated passwords are not unique."

def test_generate_passwords_content():
    """
    Test to ensure that the generated passwords contain only valid characters.
    """
    password_length = 2
    valid_characters = "AZxy09@#"
    passwords = generate_passwords(password_length)
    for password in passwords:
        assert all(c in valid_characters for c in password), "The generated passwords contain invalid characters."
