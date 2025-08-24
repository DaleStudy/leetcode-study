/**
 * N: 단어 개수, M: 평균 단어 길이
 * 시간 복잡도: O(N × M log M)
 * 공간 복잡도: O(N × M)
 */

class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val groupMap = mutableMapOf<String, MutableList<String>>()

        for (str in strs) {
            val sortedKey = str.toCharArray().sorted().joinToString("")
            groupMap.getOrPut(sortedKey) { mutableListOf()}.add(str)
        }

        return groupMap.values.toList()
    }
}
