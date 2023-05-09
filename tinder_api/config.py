import os
from dotenv import load_dotenv
load_dotenv()
TINDER_TOKEN = os.getenv('TINDER_TOKEN')
host = 'https://api.gotinder.com'
#leave tinder_token empty if you don't use phone verification
tinder_token = TINDER_TOKEN

# Your real config file should simply be named "config.py"
# Just insert your fb_username and fb_password in string format
# and the fb_auth_token.py module will do the rest!
