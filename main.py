from config.setup import setup
from config.bot import run
from config.credentials import account_name

api, user = setup(account_name)
run(user, api)
