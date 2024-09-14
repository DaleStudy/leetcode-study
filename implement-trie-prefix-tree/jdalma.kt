package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `implement-trie-prefix-tree` {

    /**
     * 영어 소문자만 입력된다.
     */
    class Trie {

        private val node = Node()

        /**
         * TC: O(n), SC: O(n)
         */
        fun insert(word: String) {
            var now = node

            for (char in word) {
                val index = char - 'a'
                if (now.next[index] == null) {
                    now.next[index] = Node()
                }
                now.next[index]?.apply { now = this }
            }
            now.isEnd = true
        }

        /**
         * TC: O(n), SC: O(1)
         */
        fun search(word: String): Boolean {
            var now = node

            for (char in word) {
                val index = char - 'a'
                if (now.next[index] == null) {
                    return false
                }
                now.next[index]?.apply { now = this }
            }

            return now.isEnd
        }

        /**
         * TC: O(n), SC: O(1)
         */
        fun startsWith(prefix: String): Boolean {
            var now = node

            for (char in prefix) {
                val index = char - 'a'
                if (now.next[index] == null) {
                    return false
                }
                now.next[index]?.apply { now = this }
            }

            return true
        }

    }

    @Test
    fun `접두사 트리를 구현하라`() {
        val trie = Trie()
        trie.insert("apple")
        trie.search("apple") shouldBe true
        trie.search("app") shouldBe false
        trie.startsWith("app") shouldBe true
        trie.insert("app")
        trie.search("app") shouldBe true
    }
}

private class Node {
    val next = Array<Node?>(26) { null }
    var isEnd = false
}
