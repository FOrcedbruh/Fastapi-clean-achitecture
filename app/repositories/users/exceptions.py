from ..exceptions import NotFoundError

class UserNotFoundError(NotFoundError):
    def __init__(self, messsage, status_code):
        super().__init__(messsage=messsage, status_code=status_code)

USER_NOT_FOUND_MESSAGE: str = "Пользователи не найдены"