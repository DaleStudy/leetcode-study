class WordDictionary {
    
    class TrieNode {
        var children: [Character: TrieNode] = [:]
        var isEndOfWord: Bool = false
    }
    
    var root: TrieNode?

    init() {
        root = TrieNode()
    }
    
    func addWord(_ word: String) {
        var currentNode = root
        for (index, char) in word.enumerated() {
            if currentNode?.children[char] == nil {
                currentNode?.children[char] = TrieNode()
            }
            currentNode = currentNode?.children[char]
            if index == word.count - 1 {
                currentNode?.isEndOfWord = true
            }
        }
    }
    
    func search(_ word: String) -> Bool {
        return dfs(root, word: word, index: 0)
    }
    
    func dfs(_ node: TrieNode?, word: String, index: Int) -> Bool {
        guard let currentNode = node else {
            return false
        }
        if index == word.count {
            return currentNode.isEndOfWord
        }
        
        let char = Array(word)[index]
        if char == "." {
            for child in currentNode.children.values {
                let result = dfs(child, word: word, index: index + 1)
                if result {
                    return true
                }
            }
        } else {
            if let child = currentNode.children[char] {
                return dfs(child, word: word, index: index + 1)
            } else {
                return false
            }
        }
        
        return false
    }
}
 
