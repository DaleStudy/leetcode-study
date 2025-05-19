class Trie:
    def __init__(self, ch):
        self.ch = ch
        self.child = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = Trie("")

    """
        - Time Complexity: O(n), n = len(word)
        - Space Complexity: O(n)
    """
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Trie(c)
            cur = cur.child[c]
        cur.isEnd = True

    """
        - Time Complexity
            - Without dot(.): O(n), n = len(word)
            - With dot(.): O(26^d), d = The number of dots
        - Space Complexity: O(n), n = len(word)
    """
    def search(self, word: str) -> bool:
        
        def dfs(node, idx):
            if len(word) == idx:
                return node.isEnd
            
            c = word[idx]
            if c == ".":
                for child in node.child.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            else:
                if c in node.child:
                    return dfs(node.child[c], idx + 1)
                else:
                    return False
                    
        return dfs(self.root, 0)

def doTest():
    wd = WordDictionary()
    wd.addWord("bad");
    wd.addWord("dad");
    wd.addWord("mad");
    assert wd.search("pad") == False, "Test Case Failed! - search('pad')"
    print("Test Case Passed! - search('pad')")
    assert wd.search("bad") == True, "Test Case Failed! - search('bad')"
    print("Test Case Passed! - search('bad')")
    assert wd.search(".ad") == True, "Test Case Failed! - search('.ad')"
    print("Test Case Passed! - search('.ad')")
    assert wd.search("b..") == True, "Test Case Failed! - search('b..')"
    print("Test Case Passed! - search('b..')")

doTest()
