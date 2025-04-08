import logging

logger = logging.getLogger(__name__)


def process_data(data):
    # ⚠️ No logging at all here
    result = [x * 2 for x in data]
    return result
