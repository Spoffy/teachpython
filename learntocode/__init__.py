from . import analytics, network
from .exception_catching import setup_excepthook

exception_catching.setup_excepthook(analytics.debug_info_handler)
