import os.path as path
import uuid

SERVER_ADDRESS = "http://127.0.0.1:8080/analytics"
USER_ID = str(uuid.getnode())
USER_ERROR_LOG_PATH = path.abspath("analytics/users")
