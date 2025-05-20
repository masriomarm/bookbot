import stats as st


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    # do something with f (the file) here


def get_report(path_to_file):
    # print report header
    header = '============ BOOKBOT ============'
    print(header)
    header = f'Analyzing book found at {path_to_file}...'
    print(header)

    header = '----------- Word Count ----------'
    print(header)
    text = get_book_text(path_to_file)
    # print(text)
    num_words = st.get_num_words(text)
    print(f"Found {num_words} total words")

    # header = '--------- Character Count -------'
    # print(header)

    num_chars = st.get_num_chars(text)
    for k, v in num_chars.items():
        print(f"{k}: {v}")


def main():
    get_report("./books/frankenstein.txt")


main()
