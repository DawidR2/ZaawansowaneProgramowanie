import csv

from model.movie import Movie
from model.link import Link
from model.rating import Rating
from model.tag import Tag


def get_all_movies() -> list:
    with open('./static/movies.csv', newline='', encoding="utf8") as csvf:
        reader = csv.DictReader(csvf)
        return [Movie(row['movieId'], row['title'], row['genres'])
                for row in reader]



def get_all_links() -> list:
    with open('./static/links.csv', newline='', encoding="utf8") as csvf:
        reader = csv.DictReader(csvf)
        return [Link(row['movieId'], row['imdbId'], row['tmdbId'])
                for row in reader]

def get_all_ratings() -> list:
    with open('./static/ratings.csv', newline='', encoding="utf8") as csvf:
        reader = csv.DictReader(csvf)
        return [Rating(row['userId'], row['movieId'], row['rating'], row['timestamp'])
                for row in reader]


def get_all_tags() -> list:
    with open('./static/tags.csv', newline='', encoding="utf8") as csvf:
        reader = csv.DictReader(csvf)
        return [Tag(row['userId'], row['movieId'], row['tag'], row['timestamp'])
                for row in reader]