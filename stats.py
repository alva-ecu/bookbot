def get_num_words(text_string):
    words_list = text_string.split()
    num_words = len(words_list)
    return num_words

def get_num_characters(text_string):
    lowercase = text_string.lower()
    char_count = {}
    for char in lowercase:
        if char in char_count:
            char_count[char] += 1
        else: char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def convert_and_sort(char_dict):
    dict_list = []
    for char in char_dict:
        new_dict = {"char": char, "num": char_dict[char]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list