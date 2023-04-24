from models.movie import Movie as MovieModel
from fastapi import HTTPException
# requerimos a Movie
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        movies = self.db.query(MovieModel).all()
        return movies
    
    def get_movie(self, movieId):
        movie = self.db.query(MovieModel).filter(MovieModel.id == movieId).first()
        if not movie:
            raise HTTPException(status_code = 404, detail = 'pelicula no encontrada')
        return movie
    
    def get_movies_by_category(self, category: str):
        movies_by_category = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return movies_by_category
    
    def create_movie(self, body: Movie):
        new_movie = MovieModel(**body.dict())
        self.db.add(new_movie)
        self.db.commit()

        return body

    def update_movie(self, movieId, body: Movie):
        movie = self.get_movie(movieId)

        movie.title = body.title
        movie.overview = body.overview
        movie.year = body.year
        movie.rating = body.rating
        movie.category = body.category

        self.db.commit()

        return body
    
    def delete_movie(self, movieId):
        movie = self.get_movie(movieId)
        self.db.delete(movie)
        self.db.commit()
        return movieId
        