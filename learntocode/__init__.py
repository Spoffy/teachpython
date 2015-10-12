from . import analytics, config, network, lessons
from .lessons import turtle, dance
from .exception_catching import setup_excepthook

exception_catching.setup_excepthook(analytics.exception_handler)
