package leetcode_study

import io.kotest.matchers.shouldBe
import leetcode_study.Type.*
import org.junit.jupiter.api.Test

class `design-add-and-search-words-data-structure` {

    class Node {
        var isEnd: Boolean = false
        val next: MutableMap<Char, Node> = mutableMapOf()
    }

    class WordDictionary {
        private val root = Node()

        /**
         * TC: O(n), SC: O(n)
         */
        fun addWord(word: String) {
            var now = root

            for (index in word.indices) {
                val node =
                    if (now.next.containsKey(word[index])) { now.next[word[index]] }
                    else Node().also { now.next[word[index]] = it }
                node?.let { now = it }
            }
            now.isEnd = true
        }

        /**
         * TC: O(26^n), SC: O(n)
         */
        fun search(word: String): Boolean {

            fun dfs(node: Node, word: String, index: Int): Boolean {
                return if (index == word.length) node.isEnd
                else if (word[index] == '.') {
                    node.next.values.any { dfs(it, word, index + 1) }
                }
                else {
                    node.next[word[index]]?.let { dfs(it, word, index + 1) } ?: false
                }
            }

            return dfs(this.root, word, 0)
        }
    }

    @Test
    fun `문자열을 저장하고 검색하는 자료구조를 구현하라`() {
        inputCommands(
            Command(ADD, "bad"),
            Command(ADD, "dad"),
            Command(ADD, "mad"),
            Command(SEARCH, "pad", false),
            Command(SEARCH, "bad", true),
            Command(SEARCH, ".ad", true),
            Command(SEARCH, "b..", true),
        )
        inputCommands(
            Command(ADD, "at"),
            Command(ADD, "and"),
            Command(ADD, "an"),
            Command(ADD, "add"),
            Command(SEARCH, "a", false),
            Command(SEARCH, ".at", false),
            Command(ADD, "bat"),
            Command(SEARCH,".at", true),
            Command(SEARCH,"an.", true),
            Command(SEARCH,"a.d.", false),
            Command(SEARCH,"b.", false),
            Command(SEARCH,"a.d", true),
            Command(SEARCH,".",  false)
        )
    }

    private fun inputCommands(vararg commands: Command) {
        val dictionary = WordDictionary()
        for (command in commands) {
            when(command.type) {
                ADD -> dictionary.addWord(command.word)
                SEARCH -> dictionary.search(command.word) shouldBe command.expect
            }
        }
    }
}

data class Command(
    val type: Type,
    val word: String,
    val expect : Boolean? = null
)

enum class Type {
    ADD, SEARCH;
}
