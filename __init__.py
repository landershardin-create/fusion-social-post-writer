# fusion_agent/__init__.py

import logging
from .core import FusionAgent
from .config import load_config
from .modules import register_modules

__version__ = "0.1.0"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fusion_agent")

# Load configuration
try:
    config = load_config()
    logger.info("Configuration loaded successfully.")
except Exception as e:
    config = {}
    logger.warning(f"Failed to load config: {e}")

# Initialize fusion agent
agent = FusionAgent(config=config)

# Register modules (e.g., finance, dashboards, contributors)
try:
    register_modules(agent)
    logger.info("Modules registered successfully.")
except Exception as e:
    logger.error(f"Module registration failed: {e}")

# Expose key components
__all__ = ["agent", "FusionAgent", "config"]
