import logging
import logging.handlers

logger = logging.getLogger('client_logger')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s: %(message)s")
name_log_file = './client_log.log'
file_handler = logging.FileHandler(name_log_file, encoding='utf-8')
file_handler.setFormatter(formatter)
file_rotater = logging.handlers.TimedRotatingFileHandler(filename=name_log_file, when='D', backupCount=7)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# logger.info("info ,essage")
# logger.debug("debug message")
# logger.error("error message")
# logger.critical("critical message")
