from .analytics import ErrorInfo
import inspect
import sys
import traceback
import os.path as path

def setup_excepthook(error_callback=None):
    def analytics_excepthook(type, value, trace):
        source_path = path.abspath(inspect.getsourcefile(trace))
        source = inspect.getsource(trace)
        error_info = ErrorInfo(type, value, trace)
        if error_callback: error_callback(error_info)

        traceback.print_exception(type, value, trace)

    sys.excepthook = analytics_excepthook

