from trie.trie import Trie

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

if __name__=="__main__":
    test_Trie()