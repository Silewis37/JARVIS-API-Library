import requests
import os
import json
from spacy.language import Language
import spacy

@Language.factory("RequestPuller")
class RequestPuller():
  def GET(url, filePath):
    response = requests.get(url)
    with open(filePath, "w+") as f:
      json.dump(response.json(), f, indent=4)