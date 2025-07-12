import logging
import os
from datetime import datetime

def setup_logging(log_file="app.log", level="level"):
    """
    Sets up basic logging for the application.

    Logs will be written to the specified log_file within a 'logs'
    subdirectory in the project root.
    """
    log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
    os.makedirs(log_directory, exist_ok=True) # Create logs directory if it doesn't exist

    log_path = os.path.join(log_directory, log_file)

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )
    #prevent duplicate logs in root logger
    logging.getLogger().handlers.clear()
    logging.getLogger().addHandler(logging.FileHandler(log_path))
    logging.getLogger().addHandler(logging.StreamHandler())
    
    logging.info(f"Logging configured. Logs will be saved to: {log_path}")

# Example usage (for testing this module)
if __name__ == "__main__":
    setup_logging(log_file=f"day3_test_log{datetime.now().strftime('%Y%m%d_%H%M%S')}.log", level=logging.DEBUG)
    logger = logging.getLogger(__name__) # Get a logger for this module 

    logger.debug("This is a DEBUG message.")
    logger.info("This is an INFO message.")
    logger.warning("This is a Warning message.")
    logger.error("This is a ERROR message.")
    logger.critical("This is a CRITICAL message.")

