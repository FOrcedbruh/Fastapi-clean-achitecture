

class NotFoundError(Exception):
    def __init__(self, messsage: str, status_code: int):
        self.message = messsage
        self.status_code = status_code



