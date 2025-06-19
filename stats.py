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