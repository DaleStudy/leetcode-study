package leetcode_study

import org.junit.jupiter.api.Test

class `valid-anagram` {

    fun isAnagram(s: String, t: String): Boolean {
        return usingArray(s, t)
    }

    // 1. 두 문자열을 정렬하여 비교한다.
    // 시간복잡도: O(n * log(n)), 공간복잡도: O(n)
    private fun usingSort(s: String, t: String): Boolean {
        val sorted1 = s.toCharArray().apply { this.sort() }
        val sorted2 = t.toCharArray().apply { this.sort() }

        return sorted1.contentEquals(sorted2)
    }

    // 2. 배열에 문자 수 가감
    // 시간복잡도: O(n), 공간복잡도: O(n)
    private fun usingArray(s: String, t: String): Boolean  {
        if (s.length != t.length) {
            return false
        }

        /* 해시맵 사용
        val map: Map<Char, Int> = mutableMapOf<Char, Int>().apply {
            (s.indices).forEach { index ->
                this[s[index]] = this.getOrDefault(s[index], 0) + 1
                this[t[index]] = this.getOrDefault(t[index], 0) - 1
            }
        }
        return map.values.find { it > 0 } == null
        */

        return IntArray(26).apply {
            for (index in s.indices) {
                this[s[index] - 'a'] = this[s[index] - 'a'] + 1
                this[t[index] - 'a'] = this[t[index] - 'a'] - 1
            }
        }.find { it > 0 } == null
    }

    @Test
    fun `입력받은 두 문자열이 애너그램이라면 참을 반환한다`() {
        isAnagram("anagram", "nagaram")
        isAnagram("test", "estt")
    }

    @Test
    fun `입력받은 두 문자열이 애너그램이 아니라면 거짓을 반환한다`() {
        isAnagram("cat", "rat")
    }
}
