import logging
import logging.handlers

logger = logging.getLogger('server_logger')
name_log_file = './server_log.log'
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s: %(message)s")
file_handler = logging.FileHandler(name_log_file, encoding='utf-8')
file_handler.setFormatter(formatter)
file_rotater = logging.handlers.TimedRotatingFileHandler(filename=name_log_file, when='D', backupCount=7)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# logger.info("info message")
# logger.debug("debug message")
# logger.error("error message")
# logger.critical("critical message")
