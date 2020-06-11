import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename="log.txt")
logging.warning('Look out!')
logging.error('Look out!')


logging.debug("Small detail. Useful for troubleshooting.")
logging.info("This is informative.")
logging.warning("This is a warning message.")
logging.error("Uh oh. Something went wrong.")
logging.critical(" We have a big problem!")

