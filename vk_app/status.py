from fastapi import HTTPException


STATUS_CODE = {
    'auth_error': HTTPException(status_code=400, detail="Authenticated error"),
    'not_found_user': HTTPException(status_code=403, detail=dict(status="error",
                                                                 code=403,
                                                                 message="Invalid account name")),
    'link_error': HTTPException(status_code=400, detail="Link require!!!"),
    'invalid_link': HTTPException(status_code=400, detail="Link invalid!!!"),
}
