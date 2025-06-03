from trie.trie import Trie
from tfidf.tfidf_search import TFIDFSearchEngine 

def test_Trie():
    trie = Trie()
    words = ["stack", "star", "start", "stark", "stair","sat","tassle"]
    for word in words:
        trie.insert(word)

    print(trie.search("star"))   # True
    print(trie.search("stair"))  # True
    print(trie.search("stamp"))  # False
    print(trie.search("tassle"))
    print(trie.autocomplete("sta"))

def test_tfidf():
    documents = [
    """Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language. In particular, it is about how to program computers to process and analyze large amounts of natural language data.""",

    """Machine learning (ML) is the study of computer algorithms that improve automatically through experience. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so.""",

    """Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning. Learning can be supervised, semi-supervised or unsupervised. Deep learning models are often trained using large datasets and powerful hardware like GPUs.""",

    """Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents. AI research deals with the question of how to create computers that are capable of intelligent behavior."""
]

    engine = TFIDFSearchEngine(documents)
    query = "artificial intelligence and machine learning"
    results = engine.score(query)

    for doc,score in results:
        print(f"Score: {score} | Document: {doc}")

if __name__=="__main__":
    test_Trie()
    test_tfidf()