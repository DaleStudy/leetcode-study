/**
 * 시간복잡도: O(L) (insert, search, startsWith 모두 동일)
 * 공간복잡도: O(ΣL × alphabetSize)
 */

class Trie() {

    private class Node {
        val child = arrayOfNulls<Node>(26)
        var isEnd: Boolean = false
    }

    private val root = Node()

    fun insert(word: String) {
        var cur = root
        for (ch in word) {
            val i = ch - 'a'
            if (cur.child[i] == null) {
                cur.child[i] = Node()
            }
            cur = cur.child[i]!!
        }
        cur.isEnd = true
    }

    fun search(word: String): Boolean {
        val node = findNode(word)
        return node?.isEnd == true
    }

    fun startsWith(prefix: String): Boolean {
        return findNode(prefix) != null
    }

    private fun findNode(s: String): Node? {
        var cur = root
        for (ch in s) {
            val i = ch - 'a'
            val next = cur.child[i] ?: return null
            cur = next
        }
        return cur
    }
}
