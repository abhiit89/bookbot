def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_book_words(filepath):
    result = get_book_text(filepath)
    return len(result.split())