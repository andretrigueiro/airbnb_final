import pymongo
import click
from flask import g
from flask.cli import with_appcontext

USERS = [
    {
        'user': 'ronaldinho',
        'password': '123',
        'email': 'ronaldinho@gmail.com',
        'type': 'host'
    },
    {
        'user': 'ronaldo',
        'password': '1234',
        'email': 'ronaldo@gmail.com',
        'type': 'guest'
    },
    {
        'user': 'rivaldo',
        'password': '12345',
        'email': 'rivaldo@gmail.com',
        'type': 'guest'
    },
]

# Initiate the Database connection
client = pymongo.MongoClient("mongodb+srv://andretrigueiro:8rMMVfyYU1c0zmgy@cluster0.ofzoa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Insert the test users contained in initi_db file
def migrate_users(db):
    db.users.insert_many(USERS)

# Command line to populate the DB with test users
@click.command('populate-db')
@with_appcontext
def populate_db_command():
    """Populate DB with data."""
    migrate_users()
    click.echo('Populated the database.')

# Initiate the database
def init_db():
    db = get_db()

# Command line to initiate the database
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Associate the db with G element
def get_db():
    if 'db' not in g:
        g.db = client.airbnb_final

    return g.db

# Close the G element
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Function to register these functions
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)