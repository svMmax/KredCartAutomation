import inspect
import logging

class Logging_Class:
    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        # defined log file
        logfile = logging.FileHandler(".\\Logs\\logfile.log")
        # defined format
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
        # defined log file --> format
        logfile.setFormatter(logformat)
        # define to add logs file
        logger.addHandler(logfile)
        # set level
        logger.setLevel(logging.INFO)
        return logger

    # Debug
    # Info
    # warning
    # error
    # critical
