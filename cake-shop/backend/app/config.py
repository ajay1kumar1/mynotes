import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb://localhost:27017/cake_shop')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'cake_shop')
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
