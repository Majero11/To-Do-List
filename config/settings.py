import os 
from dotenv import load_dotenv, find_dotenv

# find the .env file if it is in the same folder

load_dotenv(find_dotenv())

class Config:
    # Create variables in the class that will hold the values got from the .env file 
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("USER")
    DB_PASSWORD = os.getenv("PASSWORD")
    DB_HOST = os.getenv("HOST")
    DB_PORT = os.getenv("DB_PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")