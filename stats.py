def count_words(text: str) -> int:
  words = text.split()
  return len(words)

def count_letters(text: str) -> dict[str, int]:
  d = {}
  lower_text = text.lower()
  for char in lower_text:
    if char in d.keys():
      d[char] += 1
    else:
      d[char] = 1
  return d

def sort_letter_count(letter_count: dict[str, int]) -> list[dict[str, int]]:
  dict_list = []
  for key, value in letter_count.items():
    dict_list.append({"letter": key, "count": value})
  dict_list.sort(key=lambda x: x['count'], reverse=True)
  return dict_list