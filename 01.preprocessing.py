import math
import copy
import json
import string
import pandas as pd
from collections import Counter

# import the yelp review dataset
data_file = open("yelp_dataset/yelp_academic_dataset_review.json")
data = []
stop_line = 0
for line in data_file:
  if stop_line == 1000:
    break
  else:
    data.append(json.loads(line)['text'])
    stop_line += 1
data_file.close()

# Function for preprocessing string and returning text occurrence for the corresponding string
def word_preprocessing(review):
  # preprocessing step
  review = review.lower()
  escapes = ''.join([chr(char) for char in range(1, 32)])
  review = review.translate(str.maketrans('', '', escapes))
  review = review.translate(str.maketrans('', '', string.punctuation))

  return review


# Count word occurrence in a review
def word_occurrence(review):
  # word occurrence
  split_word = review.split(" ")
  word_occurence = Counter(split_word)
  
  return word_occurence
  

def remove_stopwords(review):
  # https://countwordsfree.com/stopwords
  stopwords_data = open("helpers/stop_words_english.json")
  stopwords = json.load(stopwords_data)
  rv = copy.copy(review)

  for st in stopwords:
    del rv[st]

  return rv  


# Term Frequency of words in a document
def tf(review):
  tf_dict = dict()
  total = 0
  for i in review.values():
    total += i 

  for key, val in review.items():
    tf_dict[key] = val/total

  return tf_dict


# Inverse Document Frequency  of a word over all documents
def idf(word):
  sub = 0
  for i in data:
    if word in i:
      sub += 1
  df = sub/len(data)
  idf = math.log(1/df)

  return idf


# TF-IDF values of a review
def tf_idf(tf):
  tfidf = dict()
  for key in tf.keys():
    tfidf[key] = tf[key]*idf(key) 

  return tfidf


# Take the first review
a = word_preprocessing(data[0])
b = word_occurrence(a)
print("Word occurrence of important words in a sample")
print(json.dumps(remove_stopwords(b), sort_keys=True, indent=2))

c = tf(b)
d = tf_idf(c)
print("\nTF-IDF of the sample")
print(json.dumps(d, sort_keys=True, indent=2))
