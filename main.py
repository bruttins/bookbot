def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count(file_contents)
        characters = character_count(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count(file_contents)} words found in the document")
        for character in characters:
            print(f"The '{character}' character was found {characters[character]} times")
        print("--- End report ---")

def word_count(file_contents):
    word_num = len(file_contents.split())
    return word_num

def character_count(file_contents):
    lowered_string = file_contents.lower()
    character_num = {}
    for character in lowered_string:
        if character.isalpha():
            if character in character_num:
                character_num[character] += 1
            else:
                character_num[character] = 1
    return character_num

main()