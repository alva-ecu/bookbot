import sys
from stats import get_num_words, get_num_characters, convert_and_sort

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

contents = get_book_text(book_path)
number = get_num_words(contents)
character_count = get_num_characters(contents)
sorted_list = convert_and_sort(character_count)
print("============ BOOKBOT ============") 
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {number} total words")
print("--------- Character Count -------")
for dictionary in sorted_list:
    if dictionary["char"].isalpha():
        print(f"{dictionary["char"]}: {dictionary["num"]}")
print("============= END ===============")