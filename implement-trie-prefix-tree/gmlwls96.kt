class Node() {
    val map = mutableMapOf<Char, Node?>()
    var isEnd = false
}

class Trie() {
    /** insert, search, startWith 시간 복잡도 : O(n) * */
    val rootNode = Node()
    fun insert(word: String) {
        var currentNode = rootNode
        word.forEach { char ->
            if (currentNode.map[char] == null) {
                currentNode.map[char] = Node()
            }
            currentNode = currentNode.map[char]!!
        }
        currentNode.isEnd = true
    }

    fun search(word: String): Boolean {
        var currentNode = rootNode
        word.forEach { char ->
            if (currentNode.map[char] == null) {
                return false
            } else {
                currentNode = currentNode.map[char]!!
            }
        }
        return currentNode.isEnd
    }

    fun startsWith(prefix: String): Boolean {
        var currentNode = rootNode
        prefix.forEach { char ->
            if (currentNode.map[char] == null) {
                return false
            } else {
                currentNode = currentNode.map[char]!!
            }
        }
        return true
    }
}
