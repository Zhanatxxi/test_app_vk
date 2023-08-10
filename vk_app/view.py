from fastapi import APIRouter, Query

from vk_app.exceptions import NotUserException, AnonymousInvalid, LinkException
from vk_app.status import STATUS_CODE
from vk_app.utils import get_user, get_post_info, get_10_posts_info, response_success, generate_wall_link

app_router = APIRouter(tags=["VK"])


@app_router.get("/")
def welcome(
    method: str = Query(..., enum=["profile", "likes", "posts"]),
    link: str | None = Query(None, title="post link"),
    profile: str | None = Query(None, alias_priority="profile")
):
    try:
        match method:
            case 'profile':
                data = get_user(profile)
                return response_success(data)
            case 'likes':
                if not link:
                    raise STATUS_CODE["link_error"]
                data = get_post_info(generate_wall_link(link))
                return response_success(data)
            case 'posts':
                posts, data = get_10_posts_info(profile)
                return response_success(data, posts)
    except NotUserException:
        raise STATUS_CODE["not_found_user"]
    except AnonymousInvalid:
        raise STATUS_CODE["auth_error"]
    except LinkException:
        raise STATUS_CODE["invalid_link"]
