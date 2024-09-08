def sort_on(dict):
    return dict["num"]

def main():
  BOOK_PATH = 'books/frankenstein.txt'
  with open(BOOK_PATH) as f:
    file_contents = f.read()
    words = file_contents.split()
    char_count = {}

    for word in words:
      characters = list(word.lower())
      for character in characters:
        if character.isalpha():
          char_count[character] = char_count.get(character, 0) + 1
    
    result_list = [{'character': key, 'num': value} for key, value in char_count.items()]
    result_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"{len(words)} words found in the document")
    print("\n")
    
    for result in result_list:
      print(f"The '{result['character']}' character was found {result['num']} times")

    print("--- End report ---")
main()