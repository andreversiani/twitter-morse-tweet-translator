from config.credentials import setup
from config.bot import run
from classes.user import User

api = setup()
user = User('Madokera', api)
run(user, api)