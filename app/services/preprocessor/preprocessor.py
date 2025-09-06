MODEL = "model-name"


def embed_sentence(s: str, model) -> list[float]: ...


def save_embedding(emb: list[float], db): ...


def preprocess_line(s: str) -> str: ...


def preprocess_file(filepath, db):
    with open(filepath) as file:
        for line in file:
            sentence = preprocess_line(line)
            emb = embed_sentence(sentence, model=MODEL)
            save_embedding(emb, db)
