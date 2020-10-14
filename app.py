from flask import Flask
from flask_restful import Api

from resources.summarizer import Summarizer

app = Flask(__name__)
api = Api(app)

api.add_resource(Summarizer, "/api/v1/summarize")


if __name__ == "__main__":
  app.run()
