from pydantic import BaseModel


class Counters(BaseModel):
    followers: int
    friends: int


class BaseUser(BaseModel):
    profile_id: int | None
    avatar_url: str | None


class User(BaseUser):
    followers: int | str
    following: int | str


class Likes(BaseModel):
    url: str
    likes: int
    shares: int
    views: int
    post_id: str | int

