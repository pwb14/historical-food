# Utility for adding recipes into elasticsearch
import requests
import re
import pprint

AMERICAN_COOKERY_PATTERN = r'_.+_\.'

class LoadRecipe():

    def __init__(self, file, recipe_type=None):
        self.file = file
        self.elasticsearch_url = 'http://localhost:9200/'
        self.index = "recipe"
        self.post_dict = {}
        self.recipe_content = []
        self.title_regex = re.compile(AMERICAN_COOKERY_PATTERN)

    def load_data(self):
        with open(self.file) as f:
            for line in f:
                if self.title_regex.match(line):
                    self.create_document()
                    self.post_dict["name"] = line[1:-3]
                    self.post_dict["book"] = "American Cookery"
                    self.post_dict["author_first_name"] = "Amelia"
                    self.post_dict["author_last_name"] = "Simmons"
                    self.post_dict["publication_year"] = 1796
                    self.post_dict["country_of_origin"] = "The United States of America"
                    self.post_dict["language"] = "ENG"
                else:
                    self.recipe_content.append(line)

    def create_document(self):
        if self.post_dict != {}:
            # requests.post(self.elasticsearch_url + index + "/_doc", post_dict)
            self.clean_up_content()
            # pprint.pprint(self.post_dict)
            print(self.post_dict)
            self.post_dict = {}
    
    def clean_up_content(self):
        print(self.recipe_content)
        joined_content = ''.join(self.recipe_content)
        joined_content = joined_content.replace('\n', ' ').strip()
        self.post_dict["content"] = joined_content
        self.recipe_content = []

