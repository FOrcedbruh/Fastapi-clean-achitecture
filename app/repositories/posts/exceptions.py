from ..exceptions import NotFoundError


class PostNotFoundError(NotFoundError):
    def __init__(self, messsage, status_code):
        super().__init__(messsage=messsage, status_code=status_code)

    
POST_NOT_FOUND_MESSAGE: str = "Посты не найдены"