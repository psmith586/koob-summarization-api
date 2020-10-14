from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np

#dampening factor according to page rank alg
rank_damping = 0.85
#lowest point of convergence
minimum_diff = .00001
#iteratons
runs = 100

def set_stopwords(language):
  return stopwords.words(language)

def init_matrix(sentences):
  return np.zeros([len(sentences), len(sentences)])

def normalize_matrix(sim_matrix):
  norm = np.sum(sim_matrix, axis=0)
  return np.divide(sim_matrix, norm, where = norm != 0)

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

def rank_sentences(norm_matrix):
  rank_array = np.array([1] * len(norm_matrix))
  last_rank = 0
  for x in range(runs):
    rank_array = (1 - rank_damping) + rank_damping * np.matmul(norm_matrix, rank_array)
    if abs(last_rank - sum(rank_array)) < minimum_diff:
      break
    else:
      last_rank = sum(rank_array)
  
  return rank_array

def sort_ranked(ranked):
  return list(np.argsort(ranked))


def text_rank(sentences, sentences_tokenized, language, raw_sentences):
  empty_matrix = init_matrix(sentences)
  
  if(language == "en"):
    language = "english"

  stopwords = set_stopwords(language)
  sim_matrix = build_matrix(empty_matrix, sentences_tokenized, stopwords)
  print("\n\nInitial Sim Matrix: \n", sim_matrix)
  sim_matrix += sim_matrix.T - np.diag(sim_matrix.diagonal())
  print("\n\nSquare Sim Matrix: \n", sim_matrix)
  norm_matrix = normalize_matrix(sim_matrix)
  print("\n\nNormalized Matrix: \n", norm_matrix)
  ranked = rank_sentences(norm_matrix)
  print("\n\nRanked Values: \n", ranked)
  sorted_vectors = sort_ranked(ranked)
  #sorted_vectors.reverse()
  print("\n\nSorted Sim Vectors: ", sorted_vectors)

  summary = []
  idx = 0
  for x in range(4):
    summary.append(raw_sentences[sorted_vectors[idx]])
    idx += 1

  return summary  






