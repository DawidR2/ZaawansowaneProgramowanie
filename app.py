from flask import Flask
from flask_restful import Api


from view.movie_view import MovieView
from view.link_view import LinkView
from view.rating_view import RatingView
from view.tag_view import TagView

app = Flask(__name__)
api = Api(app)

api.add_resource(MovieView, '/movies')
api.add_resource(LinkView, '/links')
api.add_resource(RatingView, '/ratings')
api.add_resource(TagView, '/tags')


if __name__ == '__main__':
    app.run(debug=True)
