def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def get_num_words(book_path):
    with open(book_path) as file:
        return file.read().split()

def get_character_counts(book_path):
    with open(book_path) as file:
        text = file.read()
        char_counts = {}
        for char in text:
            char = char.lower()
            char_counts[char] = char_counts.get(char, 0) + 1
        return char_counts
