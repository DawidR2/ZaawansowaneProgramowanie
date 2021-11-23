from flask_restful import Resource
from utils import get_all_links

class LinkView(Resource):

    def get(self):
        return [link.__dict__ for link in get_all_links()]