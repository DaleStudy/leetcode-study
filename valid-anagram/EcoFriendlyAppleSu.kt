package leetcode_study

/**
 * 문장의 문자 순서를 바꾸어 새로운 단어나 문장을 만들 수 있는지 판별하는 문제
 * 시간 복잡도: O(n)
 * -> 주어진 문자열을 순회하며 Map 자료구조에 값을 채워넣는 과정: O(n)
 * -> 알파벳 문자열 세팅 과정: O(1)
 * -> Map<알파벳, 빈도> 초기화 과정: O(1)
 * -> 알파벳 비교 과정: O(1)
 * O(1) + O(1) + O(1) + O(n) => O(n)
 *
 * 공간 복잡도: O(1)
 * -> 알파벳 빈도수를 저장 Map: O(1)
 */
fun isAnagram(s: String, t: String): Boolean {
    val alphaArray = CharArray(26) { 'a' + it}

    if (s.length != t.length) return false

    val sMap = alphaArray.associateWith { 0 }.toMutableMap()
    val tMap = alphaArray.associateWith { 0 }.toMutableMap()

    for (i in s.indices) {
        sMap[s[i]] = sMap.getValue(s[i]).plus(1)
        tMap[t[i]] = tMap.getValue(t[i]).plus(1)
    }

    for (alphabet in alphaArray) {
        if (sMap[alphabet] != tMap[alphabet]) {
            return false
        }
    }

    return true
}
