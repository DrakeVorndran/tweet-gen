from histogram import dict_histogram
import sys
import random
from pprint import pprint

def sample(histogram):
  """ returns a non-uniform random word from the histogram based on the amount the word has appeared
  expects a dict histogram """
  total = sum(histogram.values()) # adds all the values of the words in the histogram to find the total number of words
  chance = random.uniform(0, 1) # number to beat to be selected
  accumulator = 0 # total accumulated value of weighted words
  for word, count in histogram.items():
    accumulator += count/total # adds the weighted value of the word
    if accumulator > chance: # if we beat the chance, return the word
      return word

def test_sample(histogram, loops):
  """ built to run sample many times to determine the accuracy of the funciton """
  test_string = ''
  for _ in range(loops): # run sample loop number of times
    word = sample(histogram)
    test_string += " " + word # generate a large string of random words

  test_histogram = dict_histogram(test_string) # turn the test_string into a histogram
  total = sum(test_histogram.values()) # get the all the total number of words, should be equal to loop
  weighted_histogram = {} 
  for word, count in test_histogram.items(): # find the percentage each word occurs and add it to weighted_histogram
    weighted_histogram[word] = count/total

  pprint(weighted_histogram)

if __name__ == '__main__':
  test_text = 'one fish two fish red fish blue fish'
  test_histogram = dict_histogram(test_text)
  test_sample(test_histogram, int(sys.argv[1]))