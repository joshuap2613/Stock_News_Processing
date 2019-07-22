import gensim

# Load pre-trained Word2Vec model.
model = gensim.models.Word2Vec.load("Data/Vectors/SkipGram_dt=2019-07-21")
print(dir(model))
print(list(model.wv.vocab))
print(len(list(model.wv.vocab)))
#ms = model.wv.most_similar('google',10)
ms = model.most_similar(positive=['alexion', 'pharmaceuticals'], topn=200)
for x in ms:
    print (f'{x[0]}\t{x[1]}')
