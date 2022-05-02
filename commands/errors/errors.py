class IncorrectCalFormat(Exception):
    """Exception raised for errors in the input format.

    Attributes:
        `format`(str): input format which caused the error.
        `message`(str): explanation of the error.
    """
    def __init__(self, format):
        self.format = format
        self.message = """This format is incorrect.
        Theses are the avaible ones : "day", "week", "month"."""
        super().__init__(self.message)
    
    def __str__(self):
        return f""""{self.format}" -> {self.message}"""


class IncorrectTimeFormat(Exception):
    """Exception raised for errors with the format of the time (mm:ss)

    Attributes:
        `format`(str): input format which caused the error.
        `message`(str): explanation of the error.
    """
    def __init__(self, format):
        self.format = format
        self.message = """This format is incorrect.
        Correct on should be like: 01:30 (min:sec) or 30 (sec)."""
        super().__init__(self.message)
    
    def __str__(self):
        return f""""{self.format}" -> {self.message}"""