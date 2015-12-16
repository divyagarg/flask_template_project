import os
import logging
import logging.config

from config import HOME, LOG_DIR, LOG_FILE, ERROR_LOG_FILE, DEBUG_LOG_FILE


def setup_logging():
  if not os.path.exists(HOME):
    os.makedirs(HOME)

  log_dir = os.path.join(HOME, LOG_DIR)
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)

  formatter = logging.Formatter("%(asctime)s - %(levelname)s - (%(name)s) - %(message)s")

  logger = logging.getLogger('newapp')
  logger.setLevel(logging.INFO)

  handler = logging.handlers.TimedRotatingFileHandler(os.path.join(log_dir, LOG_FILE), 'midnight')
  handler.setLevel(logging.INFO)
  handler.setFormatter(formatter)

  errorhandler = logging.handlers.TimedRotatingFileHandler(os.path.join(log_dir, ERROR_LOG_FILE), 'midnight')
  errorhandler.setLevel(logging.ERROR)
  errorhandler.setFormatter(formatter)

  logger.addHandler(errorhandler)
  logger.addHandler(handler)
