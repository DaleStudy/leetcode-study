class Node() {
    val map = mutableMapOf<Char, Node?>()
    var isEnd = false
}

class WordDictionary() {

    val rootNode = Node()

    // 시간 : O(n), 공간 : O(n)
    fun addWord(word: String) {
        var currentNode = rootNode
        for (i in word.indices) {
            val char = word[i]
            if (currentNode.map[char] == null) {
                currentNode.map[char] = Node()
            }
            currentNode = currentNode.map[char]!!
        }
        currentNode.isEnd = true
    }

    // 시간 : O(26*n), 공간: O(n)
    fun search(word: String): Boolean {
        return dfs(
            pos = 0,
            word = word,
            node = rootNode
        )
    }

    fun dfs(pos: Int, word: String, node: Node): Boolean {
        var result = false
        val char = word[pos]
        val isLast = word.lastIndex == pos
        node.map.forEach {
            if (char == '.' || char == it.key) {
                if (isLast) {
                    result = true
                    return@forEach
                } else {
                    result = result or dfs(pos + 1, word, it.value!!)
                }
            }
        }
        return result
    }
}
