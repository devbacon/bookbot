from stats import get_book_text, get_num_words

book_path = 'books/frankenstein.txt'

def main():
    book_text = get_book_text(book_path)
    print(f"Book length: {len(book_text)} characters")

    book_words = get_num_words(book_path)
    print(f"Found {len(book_words)} total words")

if __name__ == "__main__":
    main()