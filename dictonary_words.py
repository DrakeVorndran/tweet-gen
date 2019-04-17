import sys
import random

words = open('/usr/share/dict/words', 'r').read()
def random_words(num):
  words_list = words.split()
  return_list = []
  for i in range(num):
    return_list.append(words_list[random.randint(0, len(words_list) - 1)])
  return return_list


if __name__ == '__main__':
  print(*random_words(int(sys.argv[1])))