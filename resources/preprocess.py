from langdetect import detect
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize

def check_lang(text):
  language = detect(text)
  return language
def set_stopwords(language):
  return stopwords.words(language)

def remove_punctuation(text):
  char_list = [char for char in text if char not in punctuation]
  return ''.join(char_list)

def remove_numbers(text):
  char_list = [char for char in text if not char.isdigit()]
  return ''.join(char_list)

def lemmatize(text, language):
  wordnet_lemmatizer = WordNetLemmatizer()
  word_tokens = word_tokenize(text)
  
  lemmatized_words = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
  return ' '.join(lemmatized_words)

def stem(text, lang):
  word_tokens = word_tokenize(text)
  snowball_stemmer = SnowballStemmer(lang)
  
  stemmed_words = [snowball_stemmer.stem(word) for word in word_tokens]
  return ' '.join(stemmed_words)

def clean_sentences(sentences):
  for x in range(len(sentences)):
    sentences[x] = remove_punctuation(sentences[x])
  return sentences  