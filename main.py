import sys
from stats import print_book_stats

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        print_book_stats(book_path)
    else:
        print("Please provide a path to a book file.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
if __name__ == "__main__":
    main()