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

def gen_sentence(chain, num_words):
  word_tuple = list(chain.keys())[randint(0,len(chain.keys())-1)]
  return_sentence = ''
  for word in word_tuple:
    return_sentence += ' ' + word
  for _ in range(num_words):
    new_word = sampling.sample(chain[word_tuple])
    return_sentence += ' ' + new_word 
    word_list = list(word_tuple[1:])
    word_list.append(new_word)
    word_tuple = tuple(word_list)
  return return_sentence

def make_pairs(corpus, order):
  output = []
  for i in range(len(corpus)-order):
    words = []
    for index in range(order):
      words.append(corpus[index+i])
    output.append((tuple(words),corpus[i+order]))
  return output

if __name__ == '__main__':
  corpus = open('ready_player_one.txt')
  text = ''
  for line in corpus:
    text +=line[:-1]+' '
  chain = gen_markov(text, 2)
  pprint(chain)
  print(gen_sentence(chain, 10))