def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    value = value.lower().replace(' ', '')
    palindrome_str = value[::-1]
    if value == palindrome_str:
        return True
    else:
        return False
