from fastapi import APIRouter , Depends
from ..controller.embedding_controller import text_embedding_controller
from ..model.TextEmbedBody import TextEmbeddBody
from ..middleware.verify_apiKey import verifyApiKey
router=APIRouter()


@router.post("/embedd-text")
async def embedd_txt(body:TextEmbeddBody,_:None=Depends(verifyApiKey)):
    return await text_embedding_controller(body)


