import stats as st
import report as fmt


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
    get_report("./books/frankenstein.txt")


main()
