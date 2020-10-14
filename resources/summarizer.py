from flask_restful import Resource, reqparse
from flask import request, jsonify

parser = reqparse.RequestParser()
parser.add_argument('text', type=str)

class Summarizer(Resource):

  def post(self):
    args = parser.parse_args()
    data = args['text']
    return data, 200
