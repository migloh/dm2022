import math
import json
import pandas as pd
import string
from collections import Counter

# import the yelp review dataset
data_file = open("yelp_dataset/yelp_academic_dataset_review.json")
data = []
stop_line = 0
for line in data_file:
  if stop_line == 100:
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

def word_occurrence(review):
  # word occurrence
  split_word = review.split(" ")
  word_occurence = Counter(split_word)
  
  return word_occurence
  

def remove_stopwords(review):
  # https://countwordsfree.com/stopwords
  stopwords_data = open("helpers/stop_words_english.json")
  stopwords = json.load(stopwords_data)

  for st in stopwords:
    del review[st]

  return review

def tf(review):
  tf_dict = dict()
  total = 0
  for i in review.values():
    total += i 

  for key, val in review.items():
    tf_dict[key] = val/total

  return tf_dict

def idf(word):
  sub = 0
  for i in data:
    if word in i:
      sub += 1
  df = sub/len(data)
  idf = math.log(1/df)

  return idf


def tf_idf(tf):
  tfidf = dict()
  for key, val in tf:
    tfidf[key] = float(val) * float(idf(key))
  
  return tfidf


       


lmeo = "If you decide to eat here, just be aware it is going to take about 2 hours from beginning to end. We have tried it multiple times, because I want to like it! I have been to it's other locations in NJ and never had a bad experience. \n\nThe food is good, but it takes a very long time to come out. The waitstaff is very young, but usually pleasant. We have just had too many experiences where we spent way too long waiting. We usually opt for another diner or restaurant on the weekends, in order to be done quicker"

a = word_preprocessing(lmeo)
b = word_occurrence(a)
c = tf(b)
d = tf_idf(c)
print(d)
