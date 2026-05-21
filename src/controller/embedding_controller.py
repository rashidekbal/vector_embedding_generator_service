from ..model.TextEmbedBody import TextEmbeddBody
from ..services.embedding_service import getTextEmbedding
from ..model.ResponseEmbedding_model import Response
from fastapi import HTTPException
async def text_embedding_controller(body:TextEmbeddBody):
    try:
        payload=body.text
        embedding=getTextEmbedding(payload)
        response =Response(status=200,message="ok",data={"payload":payload,"dimension":len(embedding),"embedding":embedding})
        return response
    except Exception as e:
        print(str(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
