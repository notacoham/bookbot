from stats import char_counter, count_words, sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = args[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_path)
    char_count = char_counter(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(sorted_dict(char_count))
    print("============= END ===============")

main() 