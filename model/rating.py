class Rating:

    def __init__(self, userId: int, movieId: str, rating: str, timestamp :str) -> None:
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp