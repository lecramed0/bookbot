import sys
from stats import wordcount, charactercount, character_report

# constants
#frank = "books/frankenstein.txt"

# functions

#def get_book_text(filepath):
#    with open(filepath) as f:
#        file_contents = f.read()
#        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    #filepath = input("provide a file path")
    #book_text = get_book_text(filepath)
    book_wordcount = wordcount(path_to_book)
    book_characters = charactercount(path_to_book)
    book_character_report = character_report(book_characters)
    print(f'''============ BOOKBOT ============
Analyzing book found at {path_to_book}...
----------- Word Count ----------
Found {book_wordcount} total words
--------- Character Count -------''')

    for character in book_character_report:
        print(f'{character["char"]}: {character["num"]}')
    print('============= END ===============')

if __name__ == "__main__":
    main()
