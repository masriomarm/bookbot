import stats as st
import report as fmt
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    # do something with f (the file) here


def get_report(path_to_file):
    text = get_book_text(path_to_file)
    num_words = st.get_num_words(text)
    num_chars = st.get_num_chars(text)

    print(fmt.format_report(text, num_words, num_chars, path_to_file))


def main():
    if sys.argv.__len__() == 2:
        get_report(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
