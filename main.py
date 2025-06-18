def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_book_words(file_content):
    return len(file_content.split())

def main():
    result = get_book_text('books/frankenstein.txt')
    num_words = get_book_words(result)
    print(f"{num_words} words found in the document")

main()