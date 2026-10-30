from stats import wc, char_count, chars_dict_to_sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_contents = get_book_text(sys.argv[1])
    word_count_of_book_contents = wc(book_contents)
    character_count = char_count(book_contents)
    sorted_list = chars_dict_to_sorted_list(character_count)
    print_report(sys.argv[1], word_count_of_book_contents, sorted_list)

def print_report(book_path, word_count, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        if item[0].isalpha():
            print(f'{item[0]}: {item[1]}')
    print("============= END ===============")

if __name__ == "__main__":
    main()
