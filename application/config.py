import os

from dotenv import load_dotenv

load_dotenv()

ARRAY_KEY_NAME = "array"
SECRET_KEY = "im-dont-want-to-use-dot-env"

# TODO здесь мог бы быть Ваш dot_env
CONTAINER_NAME = os.environ.get("CONTAINER_NAME ", "postgres")

DB_NAME = os.environ.get("DB_NAME", "admin")
DB_USER = os.environ.get("DB_USER", "admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "admin")
