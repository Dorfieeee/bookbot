def get_word_count(text):
    return len(text.split())

def get_char_counts(text):
    char_dict = {}
    for c in text:
        char = c.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_by_num(dict):
    return dict["num"]

def char_dict_to_list(char_dict):
    char_list = []
    for char in char_dict:
        temp = { "char": char, "num": char_dict[char] }
        char_list.append(temp)
    char_list.sort(reverse=True, key=sort_by_num)
    return char_list
