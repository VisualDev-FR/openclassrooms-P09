from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from LITReview.models import UserFollows, Ticket, Review
from pprint import pprint
import os, random, csv

DUMMY_PASSWORD = make_password("dummypassword")

DUMMY_USERS_FILE = os.path.join(os.path.dirname(__file__),"dummy_usernames.txt").replace('\\', '/')
DUMMY_BOOKS_FILE = os.path.join(os.path.dirname(__file__),"dummy_books.txt").replace('\\', '/')

MIN_FOLLOWS = 2
MAX_FOLLOWS = 10

MIN_TICKETS = 3
MAX_TICKETS = 10


def progress(index:int, count:int, before: str="", after: str=""):
    print("{before} {progress}% ({index}/{count}) {after}".format(
        before=before,
        progress=int(100 * (index + 1) / count),
        index=index + 1,
        count=count,
        after=after
    ) + " " * 50, end="\r" if index < count - 1 else "\n")    


def dummy_users():

    # delete all existing users
    User.objects.all().delete()

    # read all dummy usernames scrapped from https://www.magicmaman.com/prenom/
    dummy_users = open(DUMMY_USERS_FILE, "r", encoding='utf-8').readlines()

    users = []

    # create array of user
    for i, username in enumerate(dummy_users):
        users.append(
            User(username=username.replace("\n", ""), password=DUMMY_PASSWORD) 
        )
        progress(i, len(dummy_users), "Création des utilisateurs : ", username.replace("\n", ""))
    
    # register all users in database
    User.objects.bulk_create(users)


def dummy_follows():

    # delete follows database
    UserFollows.objects.all().delete()

    # create array with all users pk
    users = User.objects.all()

    # create array of userfollows
    user_follows = []

    for i, user in enumerate(users):

        for followed_user in random.sample(set(users), random.randrange(MIN_FOLLOWS, MAX_FOLLOWS)):
            user_follows.append(UserFollows(
                user = user,
                followed_user = followed_user
            ))

        progress(i, len(users), "création des abonnements : ", user.username)



    UserFollows.objects.bulk_create(user_follows)


def dummy_tickets():

    Ticket.objects.all().delete()

    user = User.objects.get(username = "Thomas")
    books = open(DUMMY_BOOKS_FILE, "r", encoding='utf-8').readlines()

    tickets = []

    for i, line in enumerate(books):
        
        line_array = line.split(";")

        title = line_array[2].strip()
        description = line_array[6].strip()
        image_url = line_array[9].strip()

        ticket = Ticket(
            user=user,
            title=title,
            description=description,
            image=image_url
        )

        tickets.append(ticket)

        progress(i, len(books), "Création des tickets : ")

    Ticket.objects.bulk_create(tickets)        


dummy_tickets()






# dummy_books = open(DUMMY_BOOKS_FILE, "r", encoding='utf-8').readlines()

# for book in dummy_books:

#     row = book.split(';')

#     title = row[0].strip()
#     description = row[1].strip()
#     image_path = os.path.join(os.path.dirname(__file__),"book_to_scrap/" + title.replace(" ", "_") + ".png").replace('\\', '/')

#     print(str(os.path.exists(image_path)) + " : " + image_path)

# for ticket in Ticket.objects.all():
#     if ticket.image.name.startswith("http")



print("\n")

