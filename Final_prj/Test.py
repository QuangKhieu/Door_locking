# from gensim.models import Word2Vec
# from sklearn.metrics.pairwise import cosine_similarity
#
# # Load pre-trained Word2Vec model (example, you should download and use a suitable pre-trained model)
# model = Word2Vec.load("path/to/your/word2vec_model")
#
# # Get embeddings for two words
# word1_embedding = model.wv["word1"]
# word2_embedding = model.wv["word2"]
#
# # Reshape to make the vectors 2D arrays
# word1_embedding = word1_embedding.reshape(1, -1)
# word2_embedding = word2_embedding.reshape(1, -1)
#
# # Calculate cosine similarity
# cosine_sim = cosine_similarity(word1_embedding, word2_embedding)[0, 0]
#
# print("Cosine Similarity between word1 and word2:", cosine_sim)
# a = ["ABC", "UIS", "SAD"]
# print(a.pop(0).lower())
# import unidecode
# def jaccard_similarity(set1, set2):
#     intersection = len(set1.intersection(set2))
#     union = len(set1.union(set2))
#     similarity = intersection / union if union != 0 else 0  # Tránh chia cho 0
#     return similarity
#
# # Ví dụ sử dụng
# set_a = set(['c', 'ó'])
# set_b = set(['c', 'o'])
#
# result = jaccard_similarity(set_a, set_b)
# print(f"Jaccard Similarity: {result}")
# a = "Có"
# # b = list(a)
# # print(b)
# print(list(unidecode.unidecode(a.lower())))

from STT_TTS import stt_tts
text = stt_tts.speech_to_text()
print(text)