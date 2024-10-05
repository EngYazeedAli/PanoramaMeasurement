from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.exception_handler import include_exception_handlers
from app.services.user_services import create_admin_user
from app.api.app_router import app_router as router


app = FastAPI()

#______________________________________________________________________________

#CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"])
#______________________________________________________________________________

#Create Admin User in The Database on Startup
app.add_event_handler("startup", create_admin_user)
#______________________________________________________________________________

#Include Customized Exception Handlers
include_exception_handlers(app)
#______________________________________________________________________________

#Include the API Router
app.include_router(router)
#______________________________________________________________________________
