from stats import count_words, num_characters, character_dict_sort
import sys

def get_book_text(filepath):
    contents: str = ""

    with open(filepath) as f:
        # f is a file object
        contents = f.read()
    return contents

def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text: str = get_book_text(sys.argv[1])
    num_words = count_words(text)
    

    characters_dict = num_characters(text)
    #print(characters_dict)
    placeholder: list = character_dict_sort(characters_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print list
    for dict in placeholder:
        if(dict["char"].isalpha()):
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()