def sort_characters(characters):
	return characters["num"]

characters = [
	{"char": "peepee", "num": 10},
	{"char": "poopoo", "num": 7},
	{"char": "peepoo", "num": 70},
	{"char": "poopee", "num": 0},	
]
characters.sort(reverse=True, key=sort_characters)


print(characters)
