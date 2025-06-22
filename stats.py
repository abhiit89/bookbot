def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_book_words(filepath):
    result = get_book_text(filepath)
    return result.split()

def get_book_words_count(filepath):
    return len(get_book_words(filepath))

def char_count(filepath):
    arr = get_book_words(filepath)
    char_map = {}
    for item in arr:
        for i in item.lower():
            if i in char_map:
                char_map[i] += 1
            else:
                char_map[i] = 1
    return char_map

def sort_on(items):
    return items["num"]

def final_dict(char_map):
    char_map_updated = []
    for key, value in char_map.items():
        temp = {}
        temp['char'] = key
        temp['num'] = value
        char_map_updated.append(temp)
    char_map_updated.sort(reverse=True, key=sort_on)
    return char_map_updated

def print_report(char_list):
    for item in char_list:
        print(f"{item['char']}: {item['num']}")