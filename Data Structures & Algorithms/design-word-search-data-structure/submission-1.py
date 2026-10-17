class WordDictionary:

    def __init__(self):
        self.trie = dict()
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = dict()
            curr = curr[c]
        curr["$"] = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return "$" in node

            c = word[index]

            if c == ".":
                for key in node:
                    if key != "$" and dfs(node[key], index +  1):
                        return True
                return False

            else:
                if c not in node:
                    return False
                return dfs(node[c], index + 1)

        return dfs(self.trie, 0)
        
