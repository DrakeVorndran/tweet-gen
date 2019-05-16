from random import choice, randint
import dictogram
import sampling
from pprint import pprint

def gen_markov(words, order=1):
  pairs = make_pairs(words.split(" "), order)
  markov_dict = {}
  for word1, word2 in pairs:
    if word1 in markov_dict:
      markov_dict[word1].add_count(word2)
    else:
      markov_dict[word1] = dictogram.Dictogram([word2])
  return markov_dict

def gen_sentence(chain):
  start_list = []
  for pair in list(chain.keys()):
    if pair[0]=="[START]":
      start_list.append(pair)
  word_tuple = start_list[randint(0,len(start_list)-1)]
  return_sentence = ''
  for word in word_tuple[1:]:
    return_sentence += ' ' + word
  while word_tuple[-1]!="[STOP]":
    new_word = sampling.sample(chain[word_tuple])
    return_sentence += ' ' + new_word 
    word_list = list(word_tuple[1:])
    word_list.append(new_word)
    word_tuple = tuple(word_list)
  return return_sentence[:-7] + '.'

def removePuncuation(text):
  punc_list = [',', '"', ':',"’","‘",'(',')']
  new_word = ''
  for _, char in enumerate(text):
    if(char not in punc_list):
      new_word += char
  return new_word

def make_pairs(corpus, order):
  output = []
  for i in range(len(corpus)-order):
    words = []
    for index in range(order):
      words.append(removePuncuation(corpus[index+i]))
    output.append((tuple(words),removePuncuation(corpus[i+order])))
  return output

if __name__ == '__main__':
  corpus = open('ready_player_one.txt')
  text = ''
  for line in corpus:
    text +=line[:-1]+' '
  chain = gen_markov(text, 2)
  # pprint(chain)
  print(gen_sentence(chain))