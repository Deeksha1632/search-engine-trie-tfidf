from trie.trie import Trie
from tfidf.tfidf_search import TFIDFSearchEngine 

#Sample documents
documents = [
    "Decision modelling is the process of creating a model to represent complex decision-making situations.",
    "Quantitative models use mathematical techniques to simulate the effects of different decisions.",
    "Optimization techniques such as linear programming help in selecting the best alternative.",
    "Uncertainty in decision modelling is addressed using probabilistic models and sensitivity analysis.",
    "Multi-criteria decision making considers multiple conflicting objectives during evaluation.",
    "Simulation is used in decision modelling to assess the performance of strategies under variable conditions.",
    "The goal of decision modelling is to improve the quality and consistency of decision-making.",
    "Decision trees are a visual and analytical support tool where decisions and possible consequences are mapped.",
    "Model validation ensures that the decision model accurately represents real-world scenarios.",
    "Software tools like Excel Solver and Analytica are used to build and analyze decision models."
]
# Initialize the search engine
engine = TFIDFSearchEngine(documents)

#Example queries
queries = ["optimization",
           "decision making",
           "uncertainty",
           "sensitivity",
           "trees",
           "simulation",
           "Excel Solver"]

for query in queries:
    print(f"\n \U0001F50D Query: {query}")
    results = engine.score(query)
    for doc_i,doc,score in results:
        print(f"Score: {score:.4f} | {doc_i+1}. {doc}")
