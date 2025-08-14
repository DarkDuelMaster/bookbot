def word_count(text_content):
	word_string = text_content.split()
	word_number = len(word_string)
	return word_number

def character_count(string_content):
	character_storage = {}
	lowercase_word_number = string_content.lower()
	for value in lowercase_word_number:
		if value not in character_storage:
			character_storage[value] = 1
		else:
			character_storage[value] = character_storage[value] + 1
	return character_storage

def sort_characters(characters):
	result = []
	for key, value in characters.items():
		result.append({"char": key, "num": value})
	result.sort(reverse=True, key=lambda x: x["num"])
	return result
