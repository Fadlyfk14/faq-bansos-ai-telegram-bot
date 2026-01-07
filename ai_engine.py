import json
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

NEW_QUESTIONS_FILE = "new_questions.json"

def save_new_question(question):
    if not os.path.exists(NEW_QUESTIONS_FILE):
        with open(NEW_QUESTIONS_FILE, "w") as f:
            json.dump([], f)

    with open(NEW_QUESTIONS_FILE, "r") as f:
        data = json.load(f)

    if question not in data:
        data.append(question)

    with open(NEW_QUESTIONS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def find_best_answer(user_text, faq_data):
    user_text = user_text.lower()

    # 1️⃣ Keyword matching
    for faq in faq_data:
        for keyword in faq["keywords"]:
            if keyword in user_text:
                return faq["answer"]

    # 2️⃣ AI similarity
    keywords = []
    answers = []

    for faq in faq_data:
        keywords.extend(faq["keywords"])
        answers.extend([faq["answer"]] * len(faq["keywords"]))

    user_embedding = model.encode([user_text])
    faq_embeddings = model.encode(keywords)

    similarity = cosine_similarity(user_embedding, faq_embeddings)
    best_idx = np.argmax(similarity)

    if similarity[0][best_idx] > 0.45:
        return answers[best_idx]

    # 3️⃣ Tidak ketemu → simpan pertanyaan
    save_new_question(user_text)
    return None