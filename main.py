

from stats import char_count, final_dict, get_book_words_count,print_report


def main():
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_book_words_count('books/frankenstein.txt')} total words")
    print('--------- Character Count -------')
    char_map = char_count('books/frankenstein.txt')
    result = final_dict(char_map)
    print_report(result)
    print('============= END ===============')
    

main()