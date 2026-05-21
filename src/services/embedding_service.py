from .embeddingModel import getTransfromer
def getTextEmbedding(text:str):
    return getTransfromer().encode(text).tolist()