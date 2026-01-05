from stats import wordcount, charactercount

# constants

frank = "books/frankenstein.txt"

# functions

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    #filepath = input("provide a file path")
    #book_text = get_book_text(filepath)
    #book_text = get_book_text("books/frankenstein.txt")
    book_wordcount = wordcount(frank)
    print(f"Found {book_wordcount} total words")
    book_characters = charactercount(frank)
    print(f"Found characters: {book_characters}")

if __name__ == "__main__":
    main()
