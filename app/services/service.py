from app.services.preprocessor import preprocessor
from app.data import test_data
from app.services.preprocessor import embed



def search():
   for sentence in test_data.dta.split("\n"):
        embedded_vector = embed.embed_sentences(sentence)
        preprocessor.upload_embeddings("HACKATHON_COLLECTION", [embedded_vector], [{"text": sentence}])