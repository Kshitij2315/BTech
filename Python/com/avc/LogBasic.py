import sys
import logging    # Every print is stored on a server
logging.basicConfig(level = logging.INFO,             # DEBUG, WARN, ERROR
                    stream = sys.stdout,
                    format = "%(asctime)s %(levelname)s:%(name)s:%(message)s",
                    datefmt = "%Y-%m-%d %H:%M:%S")
# Log level ---> which statement to print??
# Types of levels:
          # WARN
          # INFO
          # DEBUG
          # ERROR
log = logging.getLogger('myprg')

def show():
    log.info("Hello World from log.INFO")
    log.debug("This is a debug message")
    log.warning("This is a warning")
    log.error("This is a error message")
show()