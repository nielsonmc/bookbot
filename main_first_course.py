def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)
    char_report = get_character_sorted_dict(character_count)
    #print(character_count)
    #print(char_report)
    print(f"--- Begin report of {path_to_file} ---")
    #print(f"Document has {word_count} words")
    print(f"{word_count} words found in the document")
    print()
    
    for item in char_report:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    #print(words)
    return len(words)

def get_character_count(text):
    char_count = {}
    for char in text:
        #print(char)
        lowered = char.lower()
        #print(lowered)
        if lowered.isalpha():
            if lowered in char_count:
                char_count[lowered] += 1
            else:
                char_count[lowered] = 1
        #print(char_count)
    return char_count

def sort_on(dict):
    return dict["num"]

def get_character_sorted_dict(character_count):
    sorted_list = []
    for item in character_count:
        sorted_list.append({"char": item, "num": character_count[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()