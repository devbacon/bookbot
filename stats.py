book_path = 'books/frankenstein.txt'

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def get_num_words(book_path):
    with open(book_path) as file:
        return len(file.read().split())

def get_character_counts(book_path):
    with open(book_path) as file:
        text = file.read()
        char_counts = {}
        for char in text:
            if(char.isalpha()):
                char = char.lower()
                char_counts[char] = char_counts.get(char, 0) + 1
        return char_counts
    
def sort_on(item):
    return item["num"]

def get_sorted_character_counts(book_path):
    char_counts = get_character_counts(book_path)
    sorted_char_counts = []
    for char, num in char_counts.items():
        sorted_char_counts.append({"char": char, "num": num})
        sorted_char_counts.sort(reverse=True, key=sort_on)
    return sorted_char_counts

def print_book_stats(book_path):
    book_words = get_num_words(book_path)
    char_counts = get_sorted_character_counts(book_path)

    print("============ BOOKBOT ============\n" + 
        f"Analyzing book found at {book_path}...\n" +
        "----------- Word Count ----------\n" +
        f"Found {book_words} total words\n" +
        "--------- Character Count -------")
    
    for entry in char_counts:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")
