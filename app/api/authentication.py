from fastapi import Security, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from pydantic import ValidationError

security = HTTPBearer()
#___________________________________________________________________________________________________________________________________

#Authentication User Service
def authenticate(token: HTTPAuthorizationCredentials = Security(security)):
    
    try:

        payload = jwt.decode(token.credentials, "Balkan@123", algorithms = ["HS256"])

        if payload is None or "id" not in payload or "role" not in payload:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "بيانات التوكين غير صحيحة")

        id = payload.get("id")
        role = payload.get("role") 

        return {"id": id, "role": role}
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "تم انتهاء صلاحية الجلسة")
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "بيانات التوكين غير صحيحة")
#___________________________________________________________________________________________________________________________________
    
#Validate Token Service (For Manual Authentication)
def validate_token(token):
    
    try:

        payload = jwt.decode(token, "Balkan@123", algorithms = ["HS256"])

        if payload is None or "id" not in payload or "role" not in payload:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "بيانات التوكين غير صحيحة")

        id = payload.get("id")
        role = payload.get("role") 

        return {"id": id, "role": role}
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "تم انتهاء صلاحية الجلسة")
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "بيانات التوكين غير صحيحة")
#___________________________________________________________________________________________________________________________________