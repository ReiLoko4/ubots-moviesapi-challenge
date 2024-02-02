from fastapi import FastAPI
from MovieApi.connection import create_db_and_tables
from MovieApi.routes import create_movie, create_review, \
    get_movie, get_review, get_movies, get_reviews, \
    update_movie, update_review, \
    delete_movie, delete_review, root


app = FastAPI()

app.include_router(create_movie.router)
app.include_router(create_review.router)
app.include_router(get_movie.router)
app.include_router(get_review.router)
app.include_router(get_movies.router)
app.include_router(get_reviews.router)
app.include_router(update_movie.router)
app.include_router(update_review.router)
app.include_router(delete_movie.router)
app.include_router(delete_review.router)
app.include_router(root.router)


@app.on_event('startup')
async def startup_event():
    create_db_and_tables()
    print('Starting server')
