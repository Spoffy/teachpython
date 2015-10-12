from . import analytics, config, network, lessons
from .exception_catching import setup_excepthook

exception_catching.setup_excepthook(analytics.exception_handler)
