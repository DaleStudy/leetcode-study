package leetcode_study

fun groupAnagrams(strs: Array<String>): List<List<String>> {
    val anagrams = HashMap<String, MutableList<String>>()
    strs.forEach { str ->
        val chars = str.toCharArray().sorted()
        anagrams.putIfAbsent(chars.toString(), mutableListOf())
        val words = anagrams[chars.toString()]
        words?.add(str)
    }

    return anagrams.values.toList()
}
