package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

/**
 * Leetcode
 * 242. Valid Anagram
 * Easy
 */
class ValidAnagram {
    /**
     * Runtime: 24 ms(Beats: 52.77 %)
     * Time Complexity: O(n)
     *   - n: 문자열의 길이
     *
     * Memory: 38.32 MB(Beats: 31.34 %)
     * Space Complexity: O(1)
     *   - 해시맵의 크기가 알파벳 개수로 제한됨
     */
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) return false
        val map = hashMapOf<Char, Int>()
        for (i in s.indices) {
            map[s[i]] = map.getOrDefault(s[i], 0) + 1
        }
        for (i in t.indices) {
            if (map[t[i]] == null || map[t[i]] == 0) {
                return false
            }
            map[t[i]] = map.get(t[i])!! - 1
        }
        return true
    }

    /**
     * 해시맵 대신 배열을 이용한 풀이
     * Runtime: 3 ms(Beats: 99.89 %)
     * Time Complexity: O(n)
     *
     * Memory: 37.25 MB(Beats: 80.30 %)
     * Space Complexity: O(1)
     */
    fun isAnagram2(s: String, t: String): Boolean {
        if (s.length != t.length) return false
        val array = IntArray(26)
        for (i in s.indices) {
            array[s[i] - 'a']++
        }
        for (i in t.indices) {
            array[t[i] - 'a']--
        }
        for (num in array) {
            if (num != 0) {
                return false
            }
        }
        return true
    }

    @Test
    fun test() {
        isAnagram("anagram", "nagaram") shouldBe true
        isAnagram("rat", "car") shouldBe false
        isAnagram2("anagram", "nagaram") shouldBe true
        isAnagram2("rat", "car") shouldBe false
    }
}

/**
 * 개선할 여지 1.
 * 찾아보니 IntArray.all 이라는 메서드가 있어서 array.all { it == 0 } 을 사용했어도 괜찮았을 것 같아요!
 * 모든 요소가 주어진 조건을 만족하는지 검사하는 메서드라고 합니다!
 *
 * 개선할 여지 2.
 * s와 t의 문자열이 같음을 검사했으므로 첫 번째 for문에서 array[t[i] - 'a']-- 를 같이 진행해주었어도 괜찮았을 것 같아요!
 */
