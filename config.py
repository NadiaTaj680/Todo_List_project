import os

class Config:
    # SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:4321@localhost/todo_list'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
