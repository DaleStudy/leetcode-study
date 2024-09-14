package leetcode_study

import io.kotest.matchers.collections.shouldContainExactlyInAnyOrder
import org.junit.jupiter.api.Test

class `3sum` {

    fun threeSum(nums: IntArray): List<List<Int>> {
        return usingTwoPointer(nums)
    }

    /**
     * 1. 정수 배열을 순회하며 모두 확인한다. (시간초과)
     * TC: O(n^3), SC: O(n)
     */
    private fun usingIterative(nums: IntArray): List<List<Int>> {
        val result = mutableSetOf<List<Int>>()
        for (first in nums.indices) {
            for (second in first + 1 until  nums.size) {
                for (third in second + 1 until nums.size) {
                    if (nums[first] + nums[second] + nums[third] == 0) {
                        result.add(listOf(nums[first], nums[second], nums[third]).sorted())
                    }
                }
            }
        }
        return result.toList()
    }

    /**
     * 2. 입력받은 정수 배열을 정렬하여 순회하면서 원소를 합산하여 0과 비교한 결과를 기준으로 투 포인터의 값을 조작한다.
     * TC: O(n^2), SC: O(n)
     */
    private fun usingTwoPointer(nums: IntArray): List<List<Int>> {
        val sortedNumbers = nums.sorted()
        val result = mutableSetOf<List<Int>>()
        for (index in nums.indices) {
            var left = index + 1
            var right = nums.size - 1
            while (left < right) {
                val sum = sortedNumbers[index] + sortedNumbers[left] + sortedNumbers[right]
                if (sum == 0) {
                    result.add(listOf(sortedNumbers[index], sortedNumbers[left], sortedNumbers[right]))
                    left++
                    right--
                } else if (sum < 0) {
                    left++
                } else {
                    right--
                }
            }
        }
        return result.toList()
    }

    @Test
    fun `입력받은 정수 배열의 세 개의 원소의 합이 0이 되는 리스트를 반환한다`() {
        threeSum(intArrayOf(-1,0,1,2,-1,-4)) shouldContainExactlyInAnyOrder listOf(
            listOf(-1,-1,2),
            listOf(-1,0,1)
        )
        threeSum(intArrayOf(0,0,0)) shouldContainExactlyInAnyOrder listOf(
            listOf(0,0,0)
        )
    }
}
