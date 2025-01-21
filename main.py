def main():
    with open("/home/kamillentee/workspace/github.com/CamilleOnoda/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = 0
        for word in words:
            total_words += 1
            
        count_each_character(file_contents, total_words)


def count_each_character(text, total_words):
    character_count = {}
    lower_text = text.lower()

    for char in lower_text:
        if char.isalpha():
            if char not in character_count:
                character_count[char] = 1
            elif char in character_count:
                character_count[char] += 1
    
    print_report(character_count, total_words)


def print_report(character_count, total_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    for key, value in character_count.items():
        print(f"The {key} character was found {value} times")
    print("--- End of report ---")

main()
