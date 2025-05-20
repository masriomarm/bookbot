def format_chars(chars: dict):
    ret: str = ""

    header = '--------- Character Count -------'
    print(header)

    for k, v in chars.items():
        print(f"{k}: {v}", ret)

    return ret


def format_words(num_words: int):
    ret: str = ""

    header = '----------- Word Count ----------'
    print(header, ret)

    print(f"Found {num_words} total words", ret)

    return ret


def format_header(path_to_file):
    ret = ""
    header = '============ BOOKBOT ============'
    print(header, ret)
    header = f'Analyzing book found at {path_to_file}...'
    print(header, ret)

    return ret


def format_report(text, num_words, num_chars, path_to_file):
    ret = ""
    # print report header
    print(format_header(path_to_file), ret)

    print(format_words(num_words), ret)

    print(format_chars(num_chars), ret)

    return ret
