from typing import Union

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

import requests

import logging.config

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.

app = FastAPI()

class ResponseData(BaseModel):
    idUsuario: str
    internalId: int = 0

@app.get("/infoUsers/{idUsuario}", response_model=ResponseData)
def read_root(idUsuario: str):
    logger.debug("idUsuario recibido: " + idUsuario)
    
    url = 'https://63025538c6dda4f287b7ee62.mockapi.io/infoUsers/service1/'
    responseData = ResponseData(idUsuario= idUsuario)
    
    requestResult = requests.get(url + "?usuario=" + idUsuario, timeout=5)
    
    if(len(requestResult.json()) >= 1):
        responseData.internalId = requestResult.json()[0]["internalId"]
        return Response(content= responseData.json())
    else:
        return Response(status_code= status.HTTP_204_NO_CONTENT)

Instrumentator().instrument(app).expose(app) 