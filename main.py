def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    word_count = get_word_count(file_contents)
    print(f"Document has {word_count} words")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


main()