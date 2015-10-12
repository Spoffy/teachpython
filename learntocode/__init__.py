from . import analytics, config, network
from .exception_catching import setup_excepthook

exception_catching.setup_excepthook(analytics.exception_handler)
