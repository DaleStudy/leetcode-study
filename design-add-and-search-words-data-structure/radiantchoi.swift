// 단어 검색을 위한 자료구조: Trie
class WordDictionary {
    // 루트 노드
    let root: TrieNode

    init() {
        root = TrieNode()
    }
    
    func addWord(_ word: String) {
        // Array({String}) initializer의 반환 타입은 [Character]
        let spread = Array(word)
        var node = root

        // 한 글자씩 순회하며 자식 노드 추가 혹은 방문
        for letter in spread {
            if let child = node.children[letter] {
                node = child
            } else {
                let newNode = TrieNode()
                node.children[letter] = newNode
                node = newNode
            }
        }

        // 추가하고자 하는 단어의 마지막 글자에 해당하는 노드까지 순회했으므로, 해당 노드를 종료 노드로 설정
        node.isTerminating = true
    }
    
    func search(_ word: String) -> Bool {
        return traverse(root, Array(word), 0)
    }

    private func traverse(_ node: TrieNode, _ quote: [Character], _ starting: Int) -> Bool {
        // Trie의 0번째 인덱스는 아무 글자도 나타내지 않으므로, 첫 번째 글자가 곧 깊이 1의 노드에 저장
        // 따라서 starting이 quote.count와 같다면, 모든 글자를 체크한 것이므로 종료 노드인지 확인할 수 있음
        // quote.count까지 incrementing하고 바로 체크하므로, 이 이상 숫자가 커질 수 없음
        if starting == quote.count {
            return node.isTerminating
        }

        let letter = quote[starting]

        // 현재 글자가 와일드카드 문자인지 아닌지 체크하고, DFS 방식의 순회
        if letter == "." {
            var result = false

            // 와일드카드 문자라면 모든 자식 노드를 순회하여 결과 반환
            for key in node.children.keys {
                if let child = node.children[key] {
                    result = result || traverse(child, quote, starting + 1)
                }
            }

            return result
        } else {
            // 와일드카드 문자가 아니라면, 일단 자식 노드에 포함되어있는지 확인
            guard let child = node.children[letter] else {
                return false
            }

            // 포함되어있다면, 다음 글자를 순회하여 결과 반환
            return traverse(child, quote, starting + 1)
        }
    }
}

// 각각의 트라이 노드
class TrieNode {
    // 현재 글자에서 끝나는 단어가 있는가?
    var isTerminating: Bool
    // 자식 노드 - Character 형태로 다음 글자를 저장하므로, 노드에는 별도로 글자를 저장하지 않는다
    var children: [Character: TrieNode]

    init(isTerminating: Bool = false, children: [Character: TrieNode] = [:]) {
        self.isTerminating = isTerminating
        self.children = children
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary()
 * obj.addWord(word)
 * let ret_2: Bool = obj.search(word)
 */
