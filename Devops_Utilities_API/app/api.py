from fastapi import FastAPI # importing fastapi class
from routers import metrics,aws

#we will create a fastapi object to create the api
app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utitlities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version="1.1.0", #semantic versioning
    doc_url="/docs", # it will show the documentation of the api/application
    redoc_url="/redoc"
)

@app.get("/") # this is a decorator, which is an fastapi object which can convert fucntion into API endpoints.
def hello():

    """
      Hello! this is a hello api, you will see this because u r in hello api docs

    """
    #api always return dict or json
    return {"message": "Hello World ! this is devops utilities api"}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")


