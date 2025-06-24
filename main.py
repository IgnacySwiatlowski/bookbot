from stats import get_words_count, get_character_count, get_sorted_dict
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(sys.argv[1])} total words")
    print("--------- Character Count -------")
    counted = get_character_count(sys.argv[1])
    sorted_dict = get_sorted_dict(counted)
    for i in sorted_dict:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
main()