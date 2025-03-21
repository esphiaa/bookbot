# access functions from stats.py, and sys for filepath arg
from stats import *
import sys

# load the contents of the book/file
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents, file_path

# check for the file path argument
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# the big guy
def main():

    # do the thing
    book_text, file_path = get_book_text(sys.argv[1])
    word_count = get_words(book_text)
    char_counts = character_count(book_text)
    formatted = format_dicts(char_counts)
    sorted_list = sort_list(formatted)
    
    # wow who doesn't fucking love REPORTS YEAHHHH
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # sorry to all with adhd i just ruined the print wall
    # i also ruined it with a comment :)
    format_list(sorted_list)
    print("============= END ===============")

# runniititttttt les gooo
main()