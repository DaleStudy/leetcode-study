package leetcode_study

/*
* 주어진 문자열 배열에서 anagram을 그룹핑하는 문제
* 자료구조 Map을 사용해 문제 해결. 오름차순으로 정렬한 char type을 재조합해 key 값으로 사용. value는 조회 대상 문자열
* 시간 복잡도: O(n)
* 공간 복잡도: O(n)
* */
fun groupAnagrams(strs: Array<String>): List<List<String>> {
    val result = mutableMapOf<String, MutableList<String>>()

    for (str in strs) {
        val key = str.toCharArray().sorted().joinToString("")
        result.computeIfAbsent(key) { mutableListOf() }.add(str)
    }

    if (strs.isEmpty()) return listOf(listOf())
    return result.values.toList()
}
