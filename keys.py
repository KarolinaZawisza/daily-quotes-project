import os
from dotenv import load_dotenv

load_dotenv('C:/Users/zawis/Documents/EV/.env')
MAIN_EMAIL = os.getenv('main_email')
PASSWORD = os.getenv('main_email_password')
