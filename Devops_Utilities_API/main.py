#Application Entry Point

from app.api import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        # uvicorn is used in production to make our app async.
        "app.api:app",   #app -> folder/package , api.py -> file app , app -> FastAPI object
        host="0.0.0.0", #it let the api to be used by anyone of any device , host="127.0.0.1" -> localhost means run only in our system
        port=8000 ,
        reload=True  #will reload the file on any change in application 
              
    )