@echo off

call "env\Scripts\activate.bat"
start "" http://127.0.0.1:8000/feed
py.exe .\LITReview\manage.py runserver
