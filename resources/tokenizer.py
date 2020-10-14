from nltk import word_tokenize, sent_tokenize

def get_sentences(text):
  sentences = sent_tokenize(text)
  return sentences

def get_words(sentences):
  sent_words = [word_tokenize(sent) for sent in sentences]
  return sent_words

