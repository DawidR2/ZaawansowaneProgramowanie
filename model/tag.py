class Tag:

    def __init__(self, userId: int, movieId: str, tag: str, timestamp: str) -> None:
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp
