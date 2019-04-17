from pprint import pprint

def dict_histogram(string):
  words = string.split()
  histogram = {}
  for word in words:
    if word in histogram:
      histogram[word] += 1
    else:
      histogram[word] = 1
  return histogram

def LOT_histogram(string):
  dict_hist = dict_histogram(string)
  return dict_hist.items()

def LOL_histogram(string):
  tuple_hist = LOT_histogram(string)
  return_list = []
  for key, value in tuple_hist:
    return_list.append([key, value])
  return return_list

def list_of_counts(string):
  dict_hist = dict_histogram(string)
  counts_dict = {}
  for key, value in dict_hist.items():
    print(key, value)
    if value in counts_dict:
      counts_dict[value].append(key)
    else:
      counts_dict[value] = [key]
  counts_list = counts_dict.items()
  return counts_list

def frequency(word, histogram):
  return histogram[word]

def unique_words(histogram):
  return len(histogram.keys())


if __name__ == '__main__':
  book = open('book.txt', 'r').read()
  histogram = dict_histogram(book)
  pprint(histogram)
  print(unique_words(histogram))