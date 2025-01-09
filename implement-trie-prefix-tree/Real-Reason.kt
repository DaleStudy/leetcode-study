package leetcode_study

class FirstSolution {
    private val document = hashSetOf<String>()

    fun insert(word: String) {
        document.add(word)
    }

    fun search(word: String): Boolean {
        return document.contains(word)
    }

    fun startsWith(prefix: String): Boolean {
        val word = document.firstOrNull { it.startsWith(prefix) }
        return word != null
    }
}

class SecondSolution {
    class Document(var end: Boolean = true) {
        val items = hashMapOf<Char, Document>()
    }

    private val document = Document(end = true)

    fun insert(word: String) {
        var node = document
        for (char in word) {
            if (char !in node.items) {
                node.items[char] = Document(end = false)
            }
            node = node.items[char]!!
        }
        node.end = true
    }

    fun search(word: String): Boolean {
        var node = document
        for (char in word) {
            if (char !in node.items) {
                return false
            }
            node = node.items[char]!!
        }
        return node.end
    }

    fun startsWith(prefix: String): Boolean {
        var node = document
        for (char in prefix) {
            if (char !in node.items) {
                return false
            }
            node = node.items[char]!!
        }
        return true
    }
}