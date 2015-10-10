class ErrorInfo:
    def __init__(self, trace, file_path, source):
        self.trace = trace
        self.file_path = file_path
        self.source = source

    def __str__(self):
        return "\n".join([str(self.file_path), str(self.source), str(self.trace)])


