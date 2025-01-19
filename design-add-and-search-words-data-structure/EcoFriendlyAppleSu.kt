package leetcode_study


/*
* 단어 사전을 만드는 문제. (찾는 단어는 wildcard가 포함될 수 있음)
* https://www.youtube.com/watch?v=TohdsR58i3Q 동영상 참조
* trie 알고리즘을 사용한 문제 해결
* 시간 복잡도: O(L * 26)
* -> addWord() 의 경우, 각 노드는 최대 26개의 노드를 가질 수 있으며 단어의 길이가 L이라면 O(L)의 시간 소요: O(L)
* -> searchWord() 의 경우, 최악의 경우 모든 자식의 노드를 탐색해야 하므로 26(알파벳 수) 번의 탐색 진행: O(L * 26)
* 공간 복잡도: O(n * L)
* -> n 개의 단어, 평균적 단어 길이가 L일 경우 트리 노드에 저장된 노드의 수는 O(n * L)
* */
class WordDictionary() {
    // Trie 노드 클래스
    private class TrieNode {
        val children: MutableMap<Char, TrieNode> = mutableMapOf()
        var endOfWord: Boolean = false
    }

    private val root = TrieNode()

    // 단어를 트라이에 추가
    fun addWord(word: String) {
        var currentNode = root
        for (char in word) {
            if (!currentNode.children.containsKey(char)) {
                currentNode.children[char] = TrieNode()  // 해당 문자에 대한 새로운 노드 생성
            }
            currentNode = currentNode.children[char]!! // point out next trie node
        }
        currentNode.endOfWord = true  // 단어의 끝을 표시
    }

    // 주어진 패턴을 검색
    fun search(word: String): Boolean {
        return searchHelper(word, 0, root)
    }

    // 재귀적으로 단어를 검색하는 헬퍼 함수
    private fun searchHelper(word: String, index: Int, node: TrieNode): Boolean {
        if (index == word.length) {
            return node.endOfWord  // 단어의 끝에 도달했으면 해당 노드가 단어의 끝인지 확인
        }

        val char = word[index]

        if (char == '.') {  // '.'이면 모든 자식 노드에 대해 탐색
            for (childNode in node.children.values) {
                if (searchHelper(word, index + 1, childNode)) {
                    return true
                }
            }
            return false  // '.'을 처리했지만 일치하는 노드가 없으면 false
        } else {
            // 현재 문자가 존재하는 자식 노드로 계속 탐색
            val childNode = node.children[char] ?: return false
            return searchHelper(word, index + 1, childNode)
        }
    }
}
