def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    return word_count
