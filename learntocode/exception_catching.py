from .analytics import ErrorDebugInfo
import inspect, sys, traceback
import os.path as path
import sys
import traceback

def _get_source(file_path):
    try:
        with open(file_path, "r") as source_file:
            return source_file.read()
    except IOError:
        return "Unable to read source file."


def setup_excepthook(error_callback=None):
    def analytics_excepthook(type, value, trace):
        source_path = path.abspath(inspect.getsourcefile(trace))
        source = _get_source(source_path)
        formatted_trace = "".join(traceback.format_exception(type, value, trace))
        error_debug = ErrorDebugInfo(formatted_trace, source_path, source)

        if error_callback: error_callback(error_debug, type)

        traceback.print_exception(type, value, trace)

    sys.excepthook = analytics_excepthook

