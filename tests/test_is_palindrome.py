from algorithms.is_palindrome import is_palindrome

def test_basic():
    assert is_palindrome("racecar") is True
    assert is_palindrome("tomato") is False
    assert is_palindrome("별똥별") is True


def test_variants():
    assert is_palindrome("Madam") is True
    assert is_palindrome("A man a plan a canal Panama") is True