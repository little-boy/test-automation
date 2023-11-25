from string_service import to_uppercase


def test_uppercase_with_lowercased_str():
    assert to_uppercase('hello') == 'HELLO'