from FlagEmbedding import BGEM3FlagModel
from agent_rag.config.config import EmbeddingConfig

class BGEEmbedding:
    def __init__(self):
        self.embedding_model = BGEM3FlagModel(EmbeddingConfig['embedding_model_path'])

    def do_embedding(self, slices):
        print("start doing embedding !")
        embedding = self.embedding_model.encode(slices)
        print("embedding finished !")
        return embedding