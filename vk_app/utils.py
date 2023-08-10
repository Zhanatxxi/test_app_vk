import requests

from config.settings import settings
from vk_app.exceptions import NotUserException, AnonymousInvalid, LinkException
from vk_app.schemas import User, Likes


METHOD = {
    "users_get": "users.get",
    "wall_get_id": "wall.getById",
    "wall_get_posts": "wall.get"
}


NOT_DATA = "Not data, closed account"


def get_response(method, params):
    resp = requests.post(f"{settings.BASE_URL}/{method}", params=params)
    if resp.status_code == 200:
        if resp.json().get("error"):
            raise AnonymousInvalid()
        return resp.json().get("response")
    raise NotUserException("Not user")


def get_user(user_ids: int | str) -> User | Exception:

    fields = 'counters, photo_max_orig, domain'
    QUERY_PARAMS = {
        "user_ids": user_ids,
        "fields": fields,
        "v": settings.V,
        "access_token": settings.TOKEN
    }

    resp = get_response(METHOD['users_get'], QUERY_PARAMS)
    user = resp[0]
    counters = user.get("counters", {})
    return User(
        profile_id=user.get("id"),
        avatar_url=user.get("photo_max_orig", NOT_DATA),
        followers=counters.get("followers", NOT_DATA),
        following=counters.get("friends", NOT_DATA)
    )


def get_post_info(post_id: str):

    QUERY_PARAMS = {
        "posts": post_id,
        "access_token": settings.SERVICE_KEY,
        "v": settings.V
    }

    resp = get_response(METHOD['wall_get_id'], QUERY_PARAMS)
    if resp:
        return post_likes(resp[0])
    return False


def post_likes(result: dict) -> dict:
    likes_count = result.get('likes', {}).get('count', NOT_DATA)
    views_count = result.get('views', {}).get('count', NOT_DATA)
    shares_count = result.get('reposts', {}).get('count', NOT_DATA)
    post_id = result.get('id', NOT_DATA)
    owner_id = result.get('owner_id', NOT_DATA)
    full_post_id = f"{owner_id}_{post_id}"
    generate_url = f"https://vk.com/wall{full_post_id}"

    return Likes(
        url=generate_url,
        likes=likes_count,
        shares=shares_count,
        views=views_count,
        post_id=full_post_id)


def get_10_posts_info(user_ids) -> tuple[list[Likes], User]:
    data = get_user(user_ids)
    QUERY_PARAMS = {
        "access_token": settings.SERVICE_KEY,
        "owner_id": data.profile_id,
        "v": settings.V,
        "count": 10
    }

    posts = get_response(METHOD['wall_get_posts'], QUERY_PARAMS)
    posts_schemas: list[Likes] = []
    for post in posts["items"]:
        posts_schemas.append(post_likes(post))
    del data.followers
    del data.following
    return posts_schemas, data


def response_success(data, posts=None):
    if posts:
        return dict(
            status="success",
            code=200,
            data=data,
            posts=posts
        )
    return dict(
        status="success",
        code=200,
        data=data
    )


def generate_wall_link(link):
    current_link = link.split("/")
    if not current_link[-1]:
        raise LinkException()
    return current_link[-1][4:]
