from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi import Path, Query
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from libs.database import Session
from schemas.movie import Movie
from services.movie import MovieService

movie_router = APIRouter()

def get_db_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@movie_router.get('/movies', tags=['movies'], response_model = list[Movie], status_code = 200, dependencies = [Depends(JWTBearer())])
def get_movies(db: Session = Depends(get_db_session)) -> list[Movie]:
    movies = MovieService(db).get_movies()
    return JSONResponse(status_code = 200, content = jsonable_encoder(movies))

@movie_router.get('/movies/{movieId}', tags=['movies'], response_model = Movie, status_code = 200)
def get_movie(movieId: int = Path(ge = 1, le = 2000), db: Session = Depends(get_db_session)) -> Movie:
    movie = MovieService(db).get_movie(movieId)
    if not movie:
        return JSONResponse(status_code=404, content={'message': 'no se encontro la pelicula'})
    return JSONResponse(status_code=200, content=jsonable_encoder(movie))

@movie_router.get('/movies/', tags=['movies'], response_model = list[Movie], status_code = 200)
def get_movies_by_category(category: str = Query(min_length = 5, max_length=15), db: Session = Depends(get_db_session)) -> list[Movie]:
    movies_by_category = MovieService(db).get_movies_by_category(category)
    if not movies_by_category:
        return JSONResponse(status_code=404, content={'message': 'no hay registros que coincidan'})
    return JSONResponse(status_code=200, content=jsonable_encoder(movies_by_category))

@movie_router.post('/movies', tags=['movies'], response_model = dict, status_code = 201)
def create_movie(body: Movie, db: Session = Depends(get_db_session)) -> dict:
    new_movie = MovieService(db).create_movie(body)
    return JSONResponse(status_code = 200, content = {
        'message': ' movie created',
        'data': jsonable_encoder(new_movie)
    })

@movie_router.put('/movies/{movieId}', tags=['movies'], response_model = dict, status_code = 200)
def update_movie(movieId: int, body: Movie, db: Session = Depends(get_db_session)) -> dict:
    movie_updated = MovieService(db).update_movie(movieId, body)
    return JSONResponse(status_code=200, content={
        'message': 'pelicula actualizada',
        'data': jsonable_encoder(movie_updated)
    })

@movie_router.delete('/movies/{movieId}', tags=['movies'], response_model = dict, status_code = 200)
def delete_movie(movieId: int, db: Session = Depends(get_db_session)) -> dict:
    MovieService(db).delete_movie(movieId)
    return JSONResponse(status_code=200, content={
        'message': 'pelicula eliminada',
        'data': f'pelicula eliminada con id: {movieId}'
    })
 