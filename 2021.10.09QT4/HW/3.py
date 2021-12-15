def palindrome():
    with open('input.dat', 'rb') as f:
        text = f.read()
        if text == text[::-1]:
            return True
        return False
