def get_num_words(text: str):
    return text.split().__len__()


def get_num_chars(text: str):
    num_chars: dict = {}
    for word in text.lower():
        for letter in word:
            if letter.isalpha():
                num_chars[letter] = num_chars.get(letter, 0) + 1

    return num_chars
