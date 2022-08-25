import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel
from routers import cars, web
from db import engine


app = FastAPI(title='Car Sharing')
app.include_router(cars.router)
app.include_router(web.router)

@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

