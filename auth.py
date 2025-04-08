import logging

logger = logging.getLogger(__name__)


def login_user(username, password):
    logger.info(f"User login attempt: {username}")  # ⚠️ Logging username (ok), password (bad) is missing
    if username == "admin" and password == "supersecret":
        logger.info("Admin logged in successfully")
        return {"username": username}
    else:
        logger.warning("Invalid login attempt")  # ✅ Good logging
        return None
