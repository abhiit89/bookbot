
import sys
from stats import char_count, final_dict, get_book_words_count,print_report


def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    data_path =  sys.argv[1]    
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {data_path}...")
    print("----------- Word Count ----------")
    word_count = get_book_words_count(data_path)
    print(f"Found {word_count} total words")
    print('--------- Character Count -------')
    char_map = char_count(data_path)
    result = final_dict(char_map)
    print_report(result)
    print('============= END ===============')
    

main()