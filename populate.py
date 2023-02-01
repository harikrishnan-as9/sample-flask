from datetime import datetime
from app import app
from db import db

from models.user import UserModel
from models.genre import GenreModel
from models.movies import MoviesModel

with app.app_context():
    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),'populating started')

    db.drop_all()
    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),'old data and tables dropped')
    db.create_all()
    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),'new tables created')

    hari = UserModel(username='hari', password='123', role='admin')
    tom = UserModel(username='tom', password='123')

    action = GenreModel(name='Action')
    thriller = GenreModel(name='Thriller')
    comedy = GenreModel(name='Comedy')
    scifi = GenreModel(name='Sci-Fi')

    avatar = MoviesModel(title='avatar'.capitalize().replace('_', ' '), numberInStock=2, dailyRentalRate=9.5, genre=scifi)
    tenet = MoviesModel(title='tenet'.capitalize().replace('_', ' '), numberInStock=6, dailyRentalRate=7.5, genre=scifi)
    interstellar = MoviesModel(title='interstellar'.capitalize().replace('_', ' '), numberInStock=8, dailyRentalRate=6, genre=scifi)
    bean = MoviesModel(title='bean'.capitalize().replace('_', ' '), numberInStock=8, dailyRentalRate=4, genre=comedy)
    we_are_the_millers = MoviesModel(title='we_are_the_millers'.capitalize().replace('_', ' '), numberInStock=6, dailyRentalRate=4.5, genre=comedy)
    sherlock_homes = MoviesModel(title='sherlock_homes'.capitalize().replace('_', ' '), numberInStock=1, dailyRentalRate=6.5, genre=thriller)
    amoun_us = MoviesModel(title='amoun_us'.capitalize().replace('_', ' '), numberInStock=6, dailyRentalRate=2.5, genre=thriller)
    avengers = MoviesModel(title='avengers'.capitalize(), numberInStock=3, dailyRentalRate=8.5, genre=action)
    star_wars = MoviesModel(title='star_wars'.capitalize().replace('_', ' '), numberInStock=7, dailyRentalRate=7, genre=action)
    et = MoviesModel(title='ET'.replace('_', ' '), numberInStock=7, dailyRentalRate=3, genre=action)
    july_4 = MoviesModel(title='july_4'.capitalize().replace('_', ' '), numberInStock=2, dailyRentalRate=1, genre=action)

    db.session.add_all([hari, tom])
    db.session.commit()
    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),'users populated')

    db.session.add_all([action, thriller, comedy, scifi])
    db.session.commit()
    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),'genres populated')

    db.session.add_all([avatar, tenet, interstellar, bean, we_are_the_millers, sherlock_homes, amoun_us, avengers, star_wars, et])
    db.session.commit()
    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),'movies populated')

    print(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),'populating completed')


    