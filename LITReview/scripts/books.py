from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from LITReview.models import UserFollows, Ticket, Review
from pprint import pprint
import os, random
from os import listdir
from os.path import isfile, join

BOOKS_DIR = "C:/Users/menan/Desktop/OpenClassrooms/P02/openclassroom-P02/csv"
BOOKS_FILE = os.path.join(os.path.dirname(__file__),"dummy_books.txt").replace('\\', '/')


global_csv = []

for filenames in os.walk(BOOKS_DIR):
    for filename in filenames[1]:
        csv_file = os.path.join(BOOKS_DIR, filename, filename + ".csv").replace("\\", "/")

        csv_content = open(csv_file, "r", encoding="utf-8")
        csv_content.readline()

        global_csv.append(csv_content.read())

        pprint(filename)

open(BOOKS_FILE, "w", encoding="utf-8").write("".join(global_csv))

