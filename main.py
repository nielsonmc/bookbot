def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)
    #char_report = get_character_sorted_dict(char_count)
    #print(f"Document has {word_count} words")
    print(character_count)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print()
    




def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    char_count = {}
    '''
    lower_text = text.lower()
    print(lower_text)
    for char in lower_text:
        char_count[char] = lower_text.count(char)
        '''
    for char in text:
        #print(char)
        lowered = char.lower()
        #print(lowered)
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
        #print(char_count)
    return char_count


#def get_character_sorted_dict(text):


main()