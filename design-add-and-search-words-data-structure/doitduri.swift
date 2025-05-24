class WordDictionary {
    class TrieNode {
        var children: [Character: TrieNode] = [:]
        var isEndOfWord: Bool = false
    }
    
    private let root: TrieNode
    
    init() {
        root = TrieNode()
    }
    
    func addWord(_ word: String) {
        let key = word.lowercased()
        var current = root
        
        for char in key {
            if current.children[char] == nil {
                current.children[char] = TrieNode()
            }
            
            if let node = current.children[char] {
                current = node
            }
        }
        
        current.isEndOfWord = true
    }
    
    func search(_ word: String) -> Bool {
        let key = word.lowercased()
        return searchInNode(Array(key), 0, root)
    }
    
    private func searchInNode(_ word: [Character], _ index: Int, _ node: TrieNode) -> Bool {
        if index == word.count {
            return node.isEndOfWord
        }
        
        let currentChar = word[index]
        
        if currentChar == "." {
            for (_, childNode) in node.children {
                if searchInNode(word, index + 1, childNode) {
                    return true
                }
            }
            return false
        } else {
            guard let nextNode = node.children[currentChar] else {
                return false
            }
            
            return searchInNode(word, index + 1, nextNode)
        }
    }
}
