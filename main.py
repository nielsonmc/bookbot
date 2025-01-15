def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)
    print(f"Document has {word_count} words")
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    lower_text = text.lower()
    #print(lower_text)
    char_count = {}
    for char in lower_text:
        print(char)
        char_count[char] = lower_text.count(char)
        #print(char_count)
    return char_count


main()