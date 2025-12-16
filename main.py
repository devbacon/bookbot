book_path = 'books/frankenstein.txt'

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def main():
    book_text = get_book_text(book_path)
    print(f"Book length: {len(book_text)} characters")
    print(book_text)

if __name__ == "__main__":
    main()