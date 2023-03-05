from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from LITReview.models import UserFollows, Ticket
# from pprint import pprint
import os
import random

DUMMY_PASSWORD = make_password("dummypassword")

DUMMY_USERS_FILE = os.path.join(os.path.dirname(__file__), "dummy_usernames.txt").replace('\\', '/')
DUMMY_BOOKS_FILE = os.path.join(os.path.dirname(__file__), "dummy_books.txt").replace('\\', '/')

MIN_FOLLOWS = 2
MAX_FOLLOWS = 10

MIN_TICKETS = 3
MAX_TICKETS = 10

MIN_REVIEWS = 1
MAX_REVIEWS = 5


def progress(index: int, count: int, before: str = "", after: str = ""):
    """ show basic progress bar in terminal """

    print("{before} {progress}% ({index}/{count}) {after}".format(
        before=before,
        progress=int(100 * (index + 1) / count),
        index=index + 1,
        count=count,
        after=after
    ) + " " * 50, end="\r" if index < count - 1 else "\n")


def dummy_users():
    """ generate all users registered in dummy_users.txt """

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
    """ generate n randoms follows (between MIN_FOLLOWS and MAX_FOLLOWS) for each users """
    # delete follows database
    UserFollows.objects.all().delete()

    # create array with all users pk
    users = User.objects.all()

    # create array of userfollows
    user_follows = []

    for i, user in enumerate(users):

        for followed_user in random.sample(set(users), random.randrange(MIN_FOLLOWS, MAX_FOLLOWS)):
            user_follows.append(UserFollows(
                user=user,
                followed_user=followed_user
            ))

        progress(i, len(users), "création des abonnements : ", user.username)

    UserFollows.objects.bulk_create(user_follows)


def dummy_tickets():
    """ generate n randoms tickets (between MIN_TICKETS and MAX_TICKETS) for each registered users """

    Ticket.objects.all().delete()

    users = User.objects.all()
    dummy_books = open(DUMMY_BOOKS_FILE, "r", encoding='utf-8').readlines()

    tickets = []

    for i, user in enumerate(users):

        books = [
            str(line).split(";")
            for line in random.sample(set(dummy_books), random.randrange(MIN_TICKETS, MAX_TICKETS))
        ]

        for book in books:

            title = book[2].strip()
            description = book[6].strip()
            image_url = book[9].strip()

            ticket = Ticket(
                user=user,
                title=title,
                description=description,
                image=image_url
            )

            tickets.append(ticket)

        progress(i, len(users), "Création des tickets : ", user.username)

    Ticket.objects.bulk_create(tickets)


def dummy_reviews():
    """ generate n random reviews (between MIN_REVIEWS and MAX_REVIEWS) for each user """
    pass


dummy_tickets()

print("\n")
