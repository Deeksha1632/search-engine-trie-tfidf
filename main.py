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

# Initialize trie
trie = Trie()

#Insert every word into the Trie
for doc in documents:
    for word in doc.lower().split():
        trie.insert(word)

# Initialize the search engine
engine = TFIDFSearchEngine(documents)

prefix = input("🔍 Enter a prefix to search: ")
suggestions = trie.autocomplete(prefix)

# Show suggestions
'''print("\n🔤 Suggestions:")
for word in suggestions:
    print(f"• {word}")'''


# Get and show relevant documents for each suggested word
print("\n📄 Relevant Documents (Ranked by TF-IDF Score):\n")
if not suggestions:
    print(f"🔹 Word: No word found -- No relevant documents found.\n")
for word in suggestions:
    results =list(engine.score(word))
    if results:
        print(f"🔹 Word: {word}")
        for doc_no,doc,score in results[:2]: #TOP 2 docs
            print(f"   • Doc {doc_no+1}:s\"{doc}\" (Score: {score:.4f})")
        print()
    else:
        print(f"🔹 Word: {word} -- No relevant documents found.\n")