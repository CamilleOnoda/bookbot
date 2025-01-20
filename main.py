def main():
    with open("/home/kamillentee/workspace/github.com/CamilleOnoda/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()
        total_words = 0
        for word in words:
            total_words += 1
#        print(total_words)

        count_each_character(file_contents)


def count_each_character(text):
    character_count = {}
    lower_text = text.lower()

    for char in lower_text:
        if char not in character_count:
            character_count[char] = 1
        elif char in character_count:
            character_count[char] += 1
    print(character_count)


main()
