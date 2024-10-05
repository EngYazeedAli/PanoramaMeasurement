from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.api.user_api import user_router


app_router = APIRouter()


@app_router.get("/", tags = ["Redirect"])
async def redirect_to_docs(request: Request):
    return RedirectResponse(url = "/docs")



app_router.include_router(user_router, prefix = "/user", tags = ["User APIs"])
