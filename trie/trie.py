class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end_of_word
    
    def autocomplete(self,prefix):
        def DFS(trie_node,curr_pre,words):
            for key,val in trie_node.children.items():
                new_pre =  curr_pre+key
                if val.end_of_word:
                    words.append(new_pre)
                DFS(val,new_pre,words)
            return 
        curr = self.root
        for ch in prefix:
            if not curr.children[ch]:
                return []
            curr = curr.children[ch]
        ans = []
        DFS(curr,prefix,ans)
        return ans
