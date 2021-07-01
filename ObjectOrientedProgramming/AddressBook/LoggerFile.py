import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.WARNING)

logging.basicConfig(filename="ErrorLogFile.log")