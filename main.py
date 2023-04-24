from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from libs.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers import movie, user

app = FastAPI()
app.title = 'Mi APP'
app.version = 'v.01'

app.add_middleware(ErrorHandler)

#ahora incluimos los routers
app.include_router(movie.movie_router)
app.include_router(user.user_router)

Base.metadata.create_all(bind = engine)

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'accion'    
    },
    {
        'id': 2,
        'title': 'harry potter',
        'overview': "un mago travieso",
        'year': '2012',
        'rating': 6,
        'category': 'ciencia ficcion'    
    },
    {
        'id': 3,
        'title': 'supermario',
        'overview': "mario y luigi en una aventura",
        'year': '2023',
        'rating': 9.5,
        'category': 'animada'    
    },
    {
        'id': 4,
        'title': 'troya',
        'overview': "pelicula de aquiles y hector",
        'year': '2000',
        'rating': 9,
        'category': 'accion'    
    } 
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')



   
