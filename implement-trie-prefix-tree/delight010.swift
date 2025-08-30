class Trie {
    var nodes: [String: Trie] = [:]
    var isEndOfWord: Bool = false

    init() {
        
    }
    
    func insert(_ word: String) {
        if word.isEmpty {
            isEndOfWord = true
            return
        }
        
        let firstChar = String(word.first!)
        if nodes[firstChar] == nil {
            nodes[firstChar] = Trie()
        }
        nodes[firstChar]?.insert(String(word.dropFirst()))
    }
    
    func search(_ word: String) -> Bool {
        if word.isEmpty {
            return isEndOfWord
        }
        
        guard let firstChar = word.first,
              let node = nodes[String(firstChar)] else {
            return false
        }
        
        return node.search(String(word.dropFirst()))
    }
    
    func startsWith(_ prefix: String) -> Bool {
        if prefix.isEmpty {
            return true
        }
        
        guard let firstChar = prefix.first,
              let node = nodes[String(firstChar)] else {
            return false
        }
        return node.startsWith(String(prefix.dropFirst()))
    }
}
 
