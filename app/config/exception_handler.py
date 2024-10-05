from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

def include_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc: HTTPException):

        if exc.status_code == 403:
            return JSONResponse(status_code = status.HTTP_403_FORBIDDEN, 
            content = {"detail": "غير مصرح لك بالوصول إلى هذه البيانات"}
            )
        
        return JSONResponse(status_code = exc.status_code, content = {"detail": exc.detail})
