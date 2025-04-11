import sys
from stats import count_words, count_letters, sort_letter_count

def get_book_text(filepath):
  text = ""
  with open(filepath, 'r') as file:
    text = file.read()
  return text

def analyze_book(path):
  print("============ BOOKBOT ============")
  text = get_book_text(path)
  print(f"Analyzing book found at {path}...")
  
  print("----------- Word Count ----------")
  num_words = count_words(text)
  print(f"Found {num_words} total words")

  print("--------- Character Count -------")
  letter_count = count_letters(text)
  sorted_letter_count = sort_letter_count(letter_count)
  for stat in sorted_letter_count:
    if stat["letter"].isalpha():
      print(f"{stat['letter']}: {stat["count"]}")

  print("============= END ===============")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  analyze_book(book_path)

if __name__ == "__main__":
  main()