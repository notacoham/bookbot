def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    return word_count

def main():
    franken_path = "./books/frankenstein.txt"
    print(f"{count_words(franken_path)} words found in the document")
    
main()