from pydantic import BaseModel
class Response(BaseModel):
    status:int
    message:str
    data:dict|None