

from stats import get_book_words


def main():
    num_words = get_book_words('books/frankenstein.txt')
    print(f"{num_words} words found in the document")

main()