class WordDictionary {
    class TrieNode {
        var children: [Character: TrieNode] = [:]
        var isEndOfWord = false
    }
    
    private var root: TrieNode

    init() {
        root = TrieNode()
    }
    
    // O(n) time / O(n) space
    func addWord(_ word: String) {
        var node = root
        
        for character in word {
            if node.children[character] == nil {
                node.children[character] = TrieNode()
            }
            
            node = node.children[character]!
        }
        
        node.isEndOfWord = true
    }
    
    // O(m) ~ O(26^m) time / O(m) space
    func search(_ word: String) -> Bool {
        return dfs(word: Array(word), index: 0, node: root)
    }
    
    private func dfs(word: [Character], index: Int, node: TrieNode) -> Bool {
        if index == word.count {
            return node.isEndOfWord
        }
        
        let character = word[index]
        
        if character == "." {
            for child in node.children.values {
                if dfs(word: word, index: index + 1, node: child) {
                    return true
                }
            }
            return false
        } else {
            guard let child = node.children[character] else {
                return false
            }
            return dfs(word: word, index: index + 1, node: child)
        }
    }
}

