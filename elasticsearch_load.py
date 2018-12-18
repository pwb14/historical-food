# Utility for adding recipes into elasticsearch
import requests

class LoadRecipe():

    def __init__(self, file, recipe_type=None):
        self.file = file
        elasticsearch_url = 'localhost:9200'
        index = "recipe"

    def load_data(self):
        with open(self.file) as f:

    def create_document(self):

