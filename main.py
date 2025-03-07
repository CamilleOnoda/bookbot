from stats import count_num_words, count_each_character
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = open_text(book_path)
    num_words = count_num_words(text)
    characters_dict = count_each_character(text)
    sorted_dict = sort_dict(characters_dict)

    print("============ BOOKBOT ============")
    print(f"--- Analyzing book found at {book_path} ---")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    print()
    print("--- End of report ---")


def open_text(path):
    with open(path) as f:
        return f.read()


def sort_dict(dict_to_sort):
    sorted_dictionary = dict(sorted(dict_to_sort.items()))
    return sorted_dictionary

main()
