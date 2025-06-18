from stats import get_word_count, get_char_counts, char_dict_to_list
import sys


def get_book_text(path_to_book):
    with open(path_to_book) as book:
        book_contents = book.read()
        return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    book_text = get_book_text(book_path)
    book_wc = get_word_count(book_text)
    book_chars = char_dict_to_list(get_char_counts(book_text))
    print("----------- Word Count ----------")
    print(f"Found {book_wc} total words")
    print("--------- Character Count -------")
    for char_num in book_chars:
        if char_num['char'].isalpha():
            print(f"{char_num['char']}: {char_num['num']}")
    print("============= END ===============")

main()
