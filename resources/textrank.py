from nltk.cluster.util import cosine_distance
import numpy as np

def init_matrix(sentences):
  return np.zeros([len(sentences), len(sentences)])

def check_similarity(s1, s2, stopwords):
  #normalize sentence case
  s1 = [w.lower() for w in s1]
  s2 = [w.lower() for w in s2]
  #create set of the combined sentences
  unique_words = list(set(s1 + s2))
  #init vectors
  v1 = [0] * len(unique_words)
  v2 = [0] * len(unique_words)
  #add non stopwords to vectors for each sentence
  for w in s1:
    if w in stopwords:
      continue
    v1[unique_words.index(w)] += 1
    for w in s2:
      if w in stopwords:
        continue
    v2[unique_words.index(w)] += 1
        
  return 1 - cosine_distance(v1, v2)

def build_matrix(sim_matrix, sentences_tokenized, stopwords):
  #populate matrix with similarity vectors
  for x in range(len(sentences_tokenized)):
    for y in range(len(sentences_tokenized)):
      if x == y:
        continue

      sim_matrix[x][y] = check_similarity(sentences_tokenized[x], sentences_tokenized[y], stopwords)
  return sim_matrix

