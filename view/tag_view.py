from flask_restful import Resource
from utils import get_all_tags


class TagView(Resource):

    def get(self):
        return [rating.__dict__ for rating in get_all_tags()]