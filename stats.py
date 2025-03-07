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