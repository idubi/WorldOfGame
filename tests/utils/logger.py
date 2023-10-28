import logging

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    light_blue = "\x1b[94m"
    purple = "\x1b[95m"
    violet = "\x1b[38;2;238;130;238m"
    indigo= "\x1b[38;2;75;0;130m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: light_blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = 0
os = 0

def set_logger(lgr):
    global logger
    logger = lgr
    
    # logger.debug("debug message")
    # logger.info("info message")
    # logger.warning("warning message")
    # logger.error("error message")
    # logger.critical("critical message")
    


def init_main_logger():
    logger = logging.getLogger("WorkdOfGames(level 5)")
    logger.setLevel(logging.DEBUG)
    # current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ch = logging.StreamHandler()
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    set_logger(logger)


    

def get_logger():
    return logger

def set_os(o):
    global os
    os = o

def get_os():
    return os

init_main_logger()