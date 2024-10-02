def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  character = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,    
    "s": 0,
    "t": 0,    
    "u": 0,    
    "v": 0,    
    "x": 0,
    "w": 0,  
    "y": 0,
    "z": 0,
  }

  character_count = appraise_character(character, text.lower())
  sorted_characters = sorted(character_count.items(), key=lambda x: x[1], reverse=True)


  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document\n")
  for char, count in sorted_characters:
    print(f"The '{char}' character was found {count} times")
  print("--- End report ---")

def get_num_words(text):
  words = text.split()
  return len(words)


def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def appraise_character(character, text):
    for char in text:
      if char in character:
        character[char] += 1
    return character
  

main()

