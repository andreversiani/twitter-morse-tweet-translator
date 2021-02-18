from config.credentials import setup
from config.bot import run
from classes.user import User

api = setup()
name = input("Twitter account to track: ")
user = User(name, api)
run(user, api)