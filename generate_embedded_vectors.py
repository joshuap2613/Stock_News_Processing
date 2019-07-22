from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec
import datetime

CURRENT_DAY = datetime.datetime.today().strftime('%Y-%m-%d')
#reads data file
sample = open("Data/Text/2019-07-21.txt", "r")
s = sample.read()

# Replaces escape character with space
f = s.replace("\n", " ")

data = []

# iterate through each sentence in the file
for i in sent_tokenize(f):
    temp = []

    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())

    data.append(temp)

# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count = 10,
                              size = 100, window = 5)
print(len(model1.wv.vocab))
model1.save(f"Data/Vectors/CBOW_dt={CURRENT_DAY}")
# Print results
print("Cosine similarity between 'google' " +
               "and 'facebook' - CBOW : ",
    model1.similarity('google', 'facebook'))

print("Cosine similarity between 'google' " +
                 "and 'walmart' - CBOW : ",
      model1.similarity('google', 'walmart'))

# Create Skip Gram model
model2 = gensim.models.Word2Vec(data, min_count = 10, size = 100,
                                             window = 5, sg = 1)
model2.save(f"Data/Vectors/SkipGram_dt={CURRENT_DAY}")
# Print results
print("Cosine similarity between 'google' " +
          "and 'facebook' - Skip Gram : ",
    model2.similarity('google', 'facebook'))

print("Cosine similarity between 'google' " +
            "and 'walmart' - Skip Gram : ",
      model2.similarity('google', 'walmart'))

print(len(model2.wv.vocab))
