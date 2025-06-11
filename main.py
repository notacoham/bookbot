from stats import char_counter, count_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    franken_path = "./books/frankenstein.txt"

    book_text = get_book_text(franken_path)
    word_count = count_words(franken_path)
    char_count = char_counter(book_text)

    print(f"{word_count} words found in the document")
    print(char_count)

main()