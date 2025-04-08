import logging

logger = logging.getLogger(__name__)


def send_email(recipient, subject, content):
    logger.debug(f"Sending email to: {recipient}")  # ⚠️ Logging sensitive info (email address)
    logger.debug("Email content: %s", content)  # ❌ Over-logging (content might be sensitive)
    return True
