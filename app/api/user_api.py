from fastapi import APIRouter, HTTPException, Depends
from app.models.user_model import User, UpdateUser, Login
from app.services import user_services as service
from app.api.authentication import authenticate
from app.api.authentication import validate_token
from app.schemas.user_schema import user_serializer, users_list_serializer


user_router = APIRouter()

#___________________________________________________________________________________________________________________

#Get All Users API
@user_router.get("s")
async def get_all_users_api():

    try:
        
        result = await service.get_all_users()

        if result["users"]:
            return users_list_serializer(result["users"])
        
        else:
            return result

    except ValueError as error:
        raise HTTPException(status_code = 200, detail = str(error))

    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
#___________________________________________________________________________________________________________________


#Create a New User API
@user_router.post("")
async def create_user_api(user: User):

    try:
       
        created_user = user_serializer(await service.create_user(dict(user)))
        return created_user

    except ValueError as error:
        raise HTTPException(status_code = 200, detail = str(error))

    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
#___________________________________________________________________________________________________________________

#Get a User by ID API
@user_router.get("/{id}")
async def get_user_api(id: str, ):

    try:
       
        existed_user = user_serializer(await service.get_user(id))
        return  existed_user

    except ValueError as error:
        raise HTTPException(status_code = 200, detail = str(error))

    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
#___________________________________________________________________________________________________________________

#Update a User by ID API
@user_router.put("/{id}")
async def update_user_api(user: UpdateUser, id: str):

    try:
              
        updated_user = user_serializer(await service.update_user(dict(user), id))
        return updated_user

    except ValueError as error:
        raise HTTPException(status_code = 200, detail = str(error))

    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
#___________________________________________________________________________________________________________________

#Activate a User by ID API
@user_router.post("/activate/{id}")
async def activate_user_api(id: str):

    try:
       
        activated_user = await service.activate_user(id)
        return activated_user

    except ValueError as error:
        raise HTTPException(status_code = 200, detail = str(error))

    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
#___________________________________________________________________________________________________________________

#Deactivate a User by ID API
@user_router.post("/deactivate/{id}")
async def deactivate_user_api(id: str):

    try:
             
        deactivated_user = await service.deactivate_user(id)
        return deactivated_user

    except ValueError as error:
        raise HTTPException(status_code = 200, detail = str(error))

    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
#___________________________________________________________________________________________________________________

#Login API
@user_router.post("/login")
async def login_api(user: Login):

    try:
        existed_user = await service.login(dict(user))
        return existed_user

    except ValueError as error:
        raise HTTPException(status_code = 200, detail = str(error))

    except Exception as error:
        raise HTTPException(status_code = 500, detail = str(error))
#___________________________________________________________________________________________________________________
    
#Validate Token API
@user_router.post("/validate-token")
async def validate_token_api(token: str):

    token_auth = validate_token(token)
    return {"id": token_auth["id"]}
#___________________________________________________________________________________________________________________