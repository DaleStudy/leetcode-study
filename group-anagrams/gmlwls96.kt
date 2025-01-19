class Solution {

    /**
     * 시간 : O(n*wlogw), 공간 : O(n*w)
     * 풀이
     * 1. strs를 한개씩 조회하며 strs[i]를 정렬한 값을 key값, value값은 list(strs[i])형태로 추가한다.
     * 2. return 형태에 맞게 map의 value만 뽑아낸다.
     * */
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val map = mutableMapOf<String, MutableList<String>>()
        strs.forEach {
            val key = it.toCharArray()
                .sortedArray()
                .joinToString("")
            map[key] = map.getOrElse(key) { mutableListOf() }
                .apply { add(it) }
        }
        return map.map { it.value }
    }
}
