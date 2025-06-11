# Generate a random 8-character password

import secrets
import string
from loguru import logger


def generate_password(length=20):
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(char) for _ in range(20))
    return password


logger.info(f"Your new password is: {generate_password(20)}")
