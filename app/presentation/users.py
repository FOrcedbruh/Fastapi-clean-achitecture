from fastapi import APIRouter, Depends, Body
from services import UserService
from schemas.users import UserReadSchema, UserCreateSchema, UserUpdateSchema, UserReadWithPostsSchema


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserReadSchema])
async def index(
    service: UserService = Depends(UserService)
) -> list[UserReadSchema]:
    return await service.get_users()


@router.get("/{user_id}")
async def index(
    user_id: int,
    service: UserService = Depends(UserService)
) -> UserReadSchema:
    return await service.get_user(user_id=user_id)


@router.post("/create", response_model=UserReadSchema)
async def index(
    user_in: UserCreateSchema = Body(),
    service: UserService = Depends(UserService)
) -> UserReadSchema:
    return await service.create_user(user_in=user_in)


@router.patch("/update/{user_id}")
async def index(
    user_id: int,
    service: UserService = Depends(UserService),
    user_in: UserUpdateSchema = Body()
):
    return await service.update_user(user_in=user_in, user_id=user_id)
    

@router.delete("/delete/{user_id}")
async def index(
    user_id: int,
    service: UserService = Depends(UserService),
) -> dict:
    return await service.delete_user(user_id=user_id)


@router.get("/get_user_with_posts/{user_id}", response_model=list[UserReadWithPostsSchema])
async def index(
    user_id: int,
    service: UserService = Depends(UserService)
) -> list[UserReadWithPostsSchema]:
    return await service.get_user_with_posts(user_id=user_id)