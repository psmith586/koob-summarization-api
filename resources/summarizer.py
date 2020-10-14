from flask_restful import Resource, reqparse
from flask import request, jsonify

import resources.preprocess as preprocess
import resources.textrank as tr
import resources.tokenizer as tokenize

parser = reqparse.RequestParser()
parser.add_argument('text', type=str)

class Summarizer(Resource):

  def post(self):
    args = parser.parse_args()
    data = str(args['text'])
    print("Original Text: ", data)
    lang = preprocess.check_lang(data)
    lemmatized_sentences = preprocess.lemmatize(data, lang)
    print("\n\nLemmatized Text: ", lemmatized_sentences)
    sentences = tokenize.get_sentences(data)
    print("\n\nSentence Tokenize: ", sentences)
    clean_sents = preprocess.clean_sentences(sentences)
    print("\n\nSentences w/o Puntuation: ", clean_sents)
    sent_words = tokenize.get_words(clean_sents)
    print("\n\nWord Tokenized Sentences: ", sent_words)

    return jsonify(data=data, lemmatized_sentences=lemmatized_sentences, sentences=sentences, 
      clean_sents=clean_sents, sent_words=sent_words)
