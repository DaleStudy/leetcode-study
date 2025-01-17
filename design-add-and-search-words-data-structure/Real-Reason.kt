package leetcode_study

/**
 * 단어의 길이 : s
 * addWord 호출 횟수 : a
 * wildCard ('.') 의 횟수 : w
 *
 * addWord()
 * 시간복잡도 : O(s)
 * - 단어의 모든 문자열을 순회하면서 Dictionary 에 추가하므로 시간복잡도는 O(s) 입니다.
 *
 * 공간복잡도 : O(s*a)
 * - a개의 단어가 추가되고, 한 단어의 길이는 s 이므로 공간복잡도는 최대 O(s*a) 입니다.
 *
 * search()
 * 시간복잡도 : O(s * 26^2)
 * - 와일드카드가 없었을 경우 시간복잡도는 O(s) 이지만,
 * 와일드카드가 있을 때 모든 노드를 탐색하므로 26(알파벳수)개의 경우의 수가 생기며
 * 이는 최대 2번 발생 가능하다고 기재되어 있으므로 O(s * 26^2) 만큼 시간복잡도가 발생합니다.
 * */
class Dictionary(var isEnd: Boolean = false) {
    val nextChars = HashMap<Char, Dictionary>()
}
private val dictionary = Dictionary()

fun addWord(word: String) {
    var node = dictionary
    word.forEach { char ->
        if (char !in node.nextChars) {
            node.nextChars[char] = Dictionary()
        }
        node = node.nextChars[char]!!
    }

    node.isEnd = true
}

fun search(word: String): Boolean {
    var nodes = mutableListOf(dictionary)
    word.forEach { char ->
        if (char == '.') {
            nodes = nodes.flatMap { it.nextChars.values }.toMutableList()
        }
        else {
            val newNodes = mutableListOf<Dictionary>()
            nodes.forEach {
                if (char in it.nextChars) {
                    newNodes.add(it.nextChars[char]!!)
                }
            }
            nodes = newNodes
        }
    }

    return nodes.any { it.isEnd }
}
