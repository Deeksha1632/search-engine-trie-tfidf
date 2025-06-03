#TF-IDF (Term Frequency — Inverse Document Frequency) is a metric that 
#reflects how important a word is to a particular document in a 
#corpus of documents. In short, the more a word appears in a given document and the less it appears overall in an entire collection
#of documents the higher the TF-IDF score, and therefore the 
#higher the relevancy. 

# TF-IDF Formula:
# TF-IDF(term, doc) = TF(term, doc) * IDF(term)
# 
# where:
# - TF(term, doc) = (Number of times term appears in doc)
# - IDF(term) = log(N / DF(term))
#     N  = Total number of documents
#     DF = Number of documents containing the term

# TF - This word is important in this document.
# IDF - This word is not common in the entire collection.
# TF-IDF = TF*IDF 
# So, if a word gets a high Tf-IDF score -(i) It appears frequently in this document (high TDF).
#                                         (ii) It does not appear in most other documents (high IGF)

from collections import defaultdict
import math


class TFIDFSearchEngine:
    def __init__(self,documents):
        self.documents = documents
        self.N = len(documents)
        self.doc_tokens = []
        self.tf = []
        self.df = defaultdict(int)
        self.idf = {}
        self._preprocess()

    def _tokenize(self,text):
        return text.lower().split()
    
    def _preprocess(self):
        for doc in self.documents:
            tokens = self._tokenize(doc)
            self.doc_tokens.append(tokens)

            tf_dict = defaultdict(int)
            for token in tokens:
                tf_dict[token]+=1
            self.tf.append(tf_dict)

            for token in set(tokens):
                self.df[token]+=1
        
        for word in self.df:
            self.idf[word] = math.log(self.N/self.df[word])
    
    def score(self,query):
        query_tokens = self._tokenize(query)
        scores = []

        for i , tf_doc in enumerate(self.tf):
            score = 0
            for token in query_tokens:
                tf = tf_doc.get(token,0)
                idf = self.idf.get(token,0)
                score +=tf*idf
            scores.append([score,i])
        
        scores.sort(reverse=True)
        return ((self.documents[i],score) for score,i in scores if score>0)

    
