from flask_restful import Resource, reqparse
from flask import request, jsonify

import resources.preprocess as preprocess

parser = reqparse.RequestParser()
parser.add_argument('text', type=str)

class Summarizer(Resource):

  def post(self):
    args = parser.parse_args()
    data = str(args['text'])
    return jsonify(data=data)
