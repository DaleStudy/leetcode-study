package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `combination-sum` {

    /**
     * 후보자를 중복으로 사용할 수 있기에 0부터 후보자들을 누적하면서 target보다 크면 탈출하는 방식이다.
     * 만약 target과 동일하다면 누적할 때 사용된 후보자들을 numbers에 저장해뒀기에 결과에 복사한다.
     * 시간복잡도: O(n^t), 공간복잡도: O(t)
     */
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {

        fun backtracking(candidates: IntArray, target: Int, result: MutableList<List<Int>>, numbers: MutableList<Int>, start: Int, total: Int) {
            if (total > target) return
            else if (total == target) {
                result.add(numbers.toList())
            } else {
                (start until candidates.size).forEach {
                    numbers.add(candidates[it])
                    backtracking(candidates, target, result, numbers, it, total + candidates[it])
                    numbers.removeLast()
                }
            }
        }

        val result = mutableListOf<List<Int>>()
        backtracking(candidates, target, result, mutableListOf(), 0, 0)
        return result
    }

    @Test
    fun `입력받은 정수 리스트를 사용하여 목푯값을 만들어낼 수 있는 모든 경우를 리스트로 반환한다`() {
        combinationSum(intArrayOf(2,3,6,7), 7) shouldBe listOf(
            listOf(2,2,3),
            listOf(7)
        )
        combinationSum(intArrayOf(2,3,5), 8) shouldBe listOf(
            listOf(2,2,2,2),
            listOf(2,3,3),
            listOf(3,5)
        )
        combinationSum(intArrayOf(2), 1) shouldBe listOf()
    }
}
