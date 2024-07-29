with open("bangaloreriots_all_tweets.txt", "r") as f:
    sentences = f.readlines()

print(sentences)
print("@title\n" in sentences)

sentences = list(set(sentences))

with open("bangalore_tweets.txt", "w") as f:
    for sentence in sentences:
        f.write(sentence)

# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords

# stop_words = set(stopwords.words('english'))

# with open("bangaloreriots_all_tweets.txt", "r") as f:
#     sentences = f.readlines()

# unique_sentences = set(sentences)
# cleaned_sentences = []

# for sentence in unique_sentences:
#     words = sentence.split()
#     words = [word for word in words if word.lower() not in stop_words]
#     cleaned_sentence = " ".join(words)
#     cleaned_sentences.append(cleaned_sentence)

# with open("bangaloreriots_tweets.txt", "w") as f:
#     for sentence in cleaned_sentences:
#         f.write(sentence + "\n")
