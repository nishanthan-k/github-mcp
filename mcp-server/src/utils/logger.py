import logging
import logging.handlers
import os
from pathlib import Path


def setup_logging(log_level=logging.INFO):
    """
    Configure logging for the MCP server.
    
    Creates logs/ directory if it doesn't exist and sets up file + console logging
    with a custom format that doesn't interfere with MCP stdio communication.
    
    Args:
        log_level: Logging level (default: logging.INFO)
    
    Returns:
        logging.Logger: Configured logger instance
    """
    
    # Create logs directory if it doesn't exist
    logs_dir = Path(__file__).parent.parent.parent / "logs"
    logs_dir.mkdir(exist_ok=True)
    
    log_file = logs_dir / "mcp_server.log"
    
    # Create logger
    logger = logging.getLogger("mcp_server")
    logger.setLevel(log_level)
    
    # Remove any existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Define log format: timestamp | log_level | module | message
    log_format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(log_format, datefmt=date_format)
    
    # File handler - logs to file only (doesn't interfere with MCP stdio)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger


# Initialize the logger at module import
logger = setup_logging()
