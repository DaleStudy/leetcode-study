package leetcode_study

import io.kotest.matchers.collections.shouldContainExactlyInAnyOrder
import org.junit.jupiter.api.Test

class `group-anagrams` {

    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        return usingArray(strs)
    }

    /**
     * 1. 입력받은 문자열들을 문자 배열로 변환하여 정렬된 결과를 map 의 키로 정하여 키 기준으로 문자열들을 그룹화한다.
     * TC: O(n * k log(k)), SC: O(n)
     */
    private fun usingSort(strs: Array<String>): List<List<String>> {
        val map = strs.groupBy { it.toCharArray().sorted() }
        return map.values.toList()
    }

    /**
     * 2. 입력받은 문자열들을 순회하며 문자열의 문자 갯수를 카운트하여 애너그램인지 구별한다.
     * TC: O(n), SC: O(n)
     */
    private fun usingArray(strs: Array<String>): List<List<String>> {
        val map = strs.groupBy { it ->
            val counter = IntArray(26)
            for (ch in it) {
                counter[ch - 'a']++
            }
            counter.joinToString(",") // 구분자를 넣지 않으면 arrayOf("bdddddddddd","bbbbbbbbbbc") 테케를 실패함
        }

        return map.values.toList()
    }

    @Test
    fun `입력받은 문자열들을 애너그램 기준 그룹별로 반환한다`() {
        groupAnagrams(arrayOf("eat","tea","tan","ate","nat","bat")) shouldContainExactlyInAnyOrder listOf(
            listOf("tan","nat"),
            listOf("bat"),
            listOf("eat","tea","ate"),
        )
        groupAnagrams(arrayOf("cab","tin","pew","duh","may","ill","buy","bar","max","doc")) shouldContainExactlyInAnyOrder listOf(
            listOf("max"),listOf("buy"),listOf("doc"),listOf("may"),listOf("ill"),
            listOf("duh"),listOf("tin"),listOf("bar"),listOf("pew"),listOf("cab")
        )
        groupAnagrams(arrayOf("bdddddddddd","bbbbbbbbbbc")) shouldContainExactlyInAnyOrder listOf(
            listOf("bbbbbbbbbbc"),
            listOf("bdddddddddd")
        )
    }
}
