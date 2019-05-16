from pprint import pprint

def get_words(filename):
  """open the file and return a list of all words in it"""
  all_words_list = []
  with open(filename) as file:
    for line in file:
      words_list = line.split()
      for word in words_list:
        all_words_list.append(word)
  return all_words_list

def count_animals(animals_list):
  '''counts all of the occurences of unique words in a list and returns that data structure'''
  animal_counts = {}
  for animal_name in animals_list:
    if animal_name in animal_counts:
      animal_counts[animal_name] += 1
    else:
      animal_counts[animal_name] = 1
  return animal_counts

def print_table(animal_counts):
  """Prints out a table of animals and their counts"""
  print("Ainmal | Count")
  print('----------------')
  for animal_name in animal_counts:
    count = str(animal_counts[animal_name])
    print(animal_name + " | " + count)



if __name__ == "__main__":
  words = get_words('animals.txt')
  counts = count_animals(words)
  print_table(counts)
