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

def sorted_dict(dictionary):
    dict_list = []
    for item in dictionary:
        character_dictionary = {}
        if item.isalpha():
            count = dictionary[item]
            character_dictionary = {
                "char": item,
                "num": count
                }
            dict_list.append(character_dictionary)
    dict_list.sort(reverse=True, key=lambda d: d["num"])
    for list_item in dict_list:
        print(f"{list_item["char"]}: {list_item["num"]}")