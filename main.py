book_path = 'books/frankenstein.txt'

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def get_book_words(book_path):
    with open(book_path) as file:
        return file.read().split()
    
def main():
    book_text = get_book_text(book_path)
    print(f"Book length: {len(book_text)} characters")

    book_words = get_book_words(book_path)
    print(f"Found {len(book_words)} total words")

if __name__ == "__main__":
    main()