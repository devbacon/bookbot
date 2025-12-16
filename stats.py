def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def get_num_words(book_path):
    with open(book_path) as file:
        return file.read().split()
    