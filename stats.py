def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    return word_count

def char_counter(book_string):
    char_dict = {}
    for char in book_string:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1  
        else:
            char_dict[char] += 1  

    return char_dict