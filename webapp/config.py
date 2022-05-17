import os
from dotenv import load_dotenv

load_dotenv(".env")


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    COUNTRY_API_KEY = os.getenv("COUNTRY_API_KEY")
    ROZTURIZM_URL = os.getenv("ROZTURIZM_URL")
    COVID_API_URL = os.getenv("COVID_API_URL")
