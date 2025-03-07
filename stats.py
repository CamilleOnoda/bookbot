def count_num_words(text):
    words = text.split()
    total_words = 0
    for word in words:
        total_words += 1
    return total_words