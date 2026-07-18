import os
from dotenv import load_dotenv

load_dotenv()

print("DB_NAME =", os.getenv("DB_NAME"))
print("DB_USER =", os.getenv("DB_USER"))
print("DB_HOST =", os.getenv("DB_HOST"))
print("DB_PORT =", os.getenv("DB_PORT"))

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False