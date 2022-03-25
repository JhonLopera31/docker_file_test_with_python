from typing import Optional

from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__=="__main__":
    uvicorn.run(app, port=8000,host="0.0.0.0") # To work with docker the port and host mus be spicified
    #The to run the docker image the it is necessaty to set the port from the outside and the port of the container
    #docker run -p 8000:000 [image name]