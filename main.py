def main():
    book_path = "/home/kamillentee/workspace/github.com/CamilleOnoda/bookbot/books/frankenstein.txt"
    text = open_text(book_path)
    num_words = count_num_words(text)
    characters_dict = count_each_character(text)
    sorted_dict = sort_dict(characters_dict)


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for key, value in sorted_dict.items():
        print(f"The '{key}' character was found {value} times")
    print()
    print("--- End of report ---")


def open_text(path):
    with open(path) as f:
        return f.read()


def count_num_words(text):
    words = text.split()
    total_words = 0
    for word in words:
        total_words += 1
    return total_words


def count_each_character(text):
    character_count = {}
    lower_text = text.lower()

    for char in lower_text:
        if char.isalpha():
            if char not in character_count:
                character_count[char] = 1
            elif char in character_count:
                character_count[char] += 1
    
    return character_count


def sort_dict(dict_to_sort):
    sorted_dictionary = dict(sorted(dict_to_sort.items()))
    return sorted_dictionary

main()
