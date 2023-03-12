from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from LITReview.models import UserFollows, Ticket, Review
# from pprint import pprint
from datetime import datetime, timedelta
import os
import random
import typing

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


def dummy_datetime():
    return datetime(
        year=2022,
        month=random.randrange(1, 13),
        day=random.randrange(1, 28),
        hour=random.randrange(0, 23),
        minute=random.randrange(1, 59),
        second=random.randrange(1, 59)
    )


def dummy_timedelta():
    return timedelta(
        days=random.randrange(0, 10),
        hours=random.randrange(0, 23),
        minutes=random.randrange(0, 59),
        seconds=random.randrange(0, 59)
    )


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

        for followed_user in random.sample(set(users), random.randrange(MIN_FOLLOWS, MAX_FOLLOWS)):  # type: ignore
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
            for line in random.sample(set(dummy_books), random.randrange(MIN_TICKETS, MAX_TICKETS))  # type: ignore
        ]

        for book in books:

            title = book[2].strip()
            description = book[6].strip()
            image_url = book[9].strip()

            ticket = Ticket(
                user=user,
                title=title,
                description=description,
                image=image_url,
            )

            tickets.append(ticket)

        progress(i, len(users), "Création des tickets : ", user.username)

    Ticket.objects.bulk_create(tickets)


def dummy_date_ticket():

    tickets = Ticket.objects.all()

    for i, ticket in enumerate(tickets):
        ticket.time_created = dummy_datetime()
        ticket.save()
        progress(i, len(tickets), "Mise à jour de la date des tickets : ")


def dummy_reviews():
    """ generate n random reviews (between MIN_REVIEWS and MAX_REVIEWS) for each user """

    dummy_reviews = {
        0: {
            "headline": "C'était nul !",
            "rating": 0,
            "body": "A fuir ! ce livre est ennuyant au possible !"
        },
        1: {
            "headline": "Pas top...",
            "rating": 1,
            "body": "Globalement sans interêt.."
        },
        2: {
            "headline": "Bof...",
            "rating": 2,
            "body": "Quel dommage de gacher une histoire si originale..."
        },
        3: {
            "headline": "La fin est décevante",
            "rating": 3,
            "body": "La fin aurait mérité d'être mieux travaillée..."
        },
        4: {
            "headline": "Très sympa !",
            "rating": 4,
            "body": "Rafraichissant et captivant !"
        },
        5: {
            "headline": "INCROYABLE !",
            "rating": 5,
            "body": "Je n'ai jamais été aussi captivé par un livre !"
        },
    }

    Review.objects.all().delete()

    users = User.objects.all()

    reviews = []

    for i, user in enumerate(users):

        accessible_tickets: typing.List[Ticket] = []

        for userfollow in UserFollows.objects.filter(user=user):
            accessible_tickets.extend(
                Ticket.objects.filter(
                    user=userfollow.followed_user
                )
            )

        for ticket in random.sample(
            set(accessible_tickets),
            random.randrange(MIN_REVIEWS, MAX_REVIEWS)
        ):  # type: ignore

            random_review = dummy_reviews[random.randrange(0, 5)]

            reviews.append(
                Review(
                    user=user,
                    ticket=ticket,
                    rating=random_review['rating'],
                    headline=random_review['headline'],
                    body=random_review['body'],
                )
            )

        progress(i, len(users), "Création des reviews", user.username)

    Review.objects.bulk_create(reviews)

    # time_created=ticket.time_created + dummy_timedelta()


def dummy_date_reviews():

    reviews = Review.objects.all()

    for i, review in enumerate(reviews):
        review.time_created = review.ticket.time_created + dummy_timedelta()
        review.save()
        progress(i, len(reviews), "Mise à jour de la date des reviews : ")


dummy_tickets()
dummy_date_ticket()
dummy_reviews()
dummy_date_reviews()


print("\n")
