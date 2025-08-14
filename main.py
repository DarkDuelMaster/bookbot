import sys
from stats import word_count
from stats import character_count
from stats import sort_characters

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(path_to_file):
	with open(path_to_file) as f: file_contents = f.read()
	return file_contents

def main():
	book = get_book_text(path_to_file)
	num_word = word_count(book)
	char_counts = character_count(book)
	sorted_chars = sort_characters(char_counts)
	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {path_to_file}...")
	print ("----------- Word Count ----------")
	print (f"Found {num_word} total words")
	print ("--------- Character Count -------")
	for item in sorted_chars:
    		if item["char"].isalpha():
        		print(f"{item['char']}: {item['num']}")
	print ("============= END ===============")

main()
