import os
from dotenv import load_dotenv
load_dotenv()
MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb://localhost:27017/netflix_clone')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'netflix_clone')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30))
