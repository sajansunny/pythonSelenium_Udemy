import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logFile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.CRITICAL)

    logger.debug("This is a debug statement")
    logger.info("This is an information about the test")
    logger.warning("This is a warning about the test")
    logger.error("This is an error message")
    logger.critical("A critical error happened in your test")
