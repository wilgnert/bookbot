def get_book_text(filepath):
  text = ""
  with open(filepath, 'r') as file:
    text = file.read()
  return text

def main():
  text = get_book_text('books/frankenstein.txt')
  print(text)

if __name__ == "__main__":
  main()