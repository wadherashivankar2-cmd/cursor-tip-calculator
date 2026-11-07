def is_palindrome(text):
    # Keep letters and digits only, and ignore capitalization.
    cleaned = "".join(character.lower() for character in text if character.isalnum())
    # A palindrome reads the same forward and backward.
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # "A man, a plan, a canal: Panama" is a classic palindrome once punctuation is ignored.
    sample = "A man, a plan, a canal: Panama"
    assert is_palindrome(sample) is True
    assert is_palindrome("race a car") is False
    print(f"{sample!r} is a palindrome.")
