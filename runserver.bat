@echo off

call "env\Scripts\activate.bat"
py.exe .\LITReview\manage.py runserver
start "" http://127.0.0.1:8000/feed