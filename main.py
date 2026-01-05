from stats import wordcount, charactercount, character_report

# constants

frank = "books/frankenstein.txt"

# functions

#def get_book_text(filepath):
#    with open(filepath) as f:
#        file_contents = f.read()
#        return file_contents

def main():
    #filepath = input("provide a file path")
    #book_text = get_book_text(filepath)
    book_wordcount = wordcount(frank)
    book_characters = charactercount(frank)
    book_character_report = character_report(book_characters)
    print(f'''============ BOOKBOT ============
Analyzing book found at {frank}...
----------- Word Count ----------
Found {book_wordcount} total words
--------- Character Count -------''')

    for character in book_character_report:
        print(f'{character["char"]}: {character["num"]}')
    print('============= END ===============')

if __name__ == "__main__":
    main()
