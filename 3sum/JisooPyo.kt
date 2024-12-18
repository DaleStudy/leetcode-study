package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

/**
 * Leetcode
 * 15. 3Sum
 * Medium
 */
class `3Sum` {
    /**
     * 3중 for문으로 풀어봤는데 시간 초과가 되더라고요(당연)
     * 사실 잘 모르겠어서 Topic과 힌트를 살짝 봤는데 투 포인터가 있길래 이걸 이용해서 풀어보기로 했습니다!
     *
     * Runtime: 72 ms(Beats: 60.54 %)
     * Time Complexity: O(n^2)
     *
     * Memory: 56.28 MB(Beats: 49.51 %)
     * Space Complexity: O(n^2)
     */
    fun threeSum(nums: IntArray): List<List<Int>> {
        val answer = mutableListOf<List<Int>>()
        // 배열 정렬 - 중복된 경우를 제거하고 효율적으로 탐색하기 위하여
        nums.sort()

        // nums[i]의 이전 값을 의미합니다.
        var prev = Integer.MIN_VALUE
        for (i in nums.indices) {
            // 이전 값과 동일한 값이라면 스킵하여 중복된 경우를 제거합니다.
            if (nums[i] == prev) {
                continue
            }

            // 투 포인터 알고리즘을 이용하여 다 더하여 0이 되는 경우의 수를 찾습니다.
            var left = i + 1
            var right = nums.size - 1
            while (left < right) {

                if (nums[i] + nums[left] + nums[right] > 0) {           // 합이 0보다 크다면 right를 줄입니다.
                    // if 내에 있는 while문들은 중복 경우의 수를 피하기 위함입니다.
                    while (0 <= right - 1 && nums[right - 1] == nums[right]) {
                        right--
                    }
                    right--
                } else if (nums[i] + nums[left] + nums[right] < 0) {    // 합이 0보다 적다면 left를 높입니다.
                    while (left + 1 <= nums.size - 1 && nums[left] == nums[left + 1]) {
                        left++
                    }
                    left++
                } else {        // 합이 0이라면 경우의 수를 추가합니다.
                    answer.add(listOf(nums[i], nums[left], nums[right]))
                    while (left + 1 <= nums.size - 1 && nums[left] == nums[left + 1]) {
                        left++
                    }
                    left++
                    while (0 <= right - 1 && nums[right - 1] == nums[right]) {
                        right--
                    }
                    right--
                }
            }
            prev = nums[i]
        }
        return answer
    }

    /**
     * 시간 복잡도나 공간 복잡도가 개선되진 않았지만 가독성 측면에서 개선해본 버전입니다.
     * Runtime: 66 ms(Beats: 65.59 %)
     * Time Complexity: O(n^2)
     *
     * Memory: 56.64 MB(Beats: 43.12 %)
     * Space Complexity: O(n^2)
     */
    fun threeSum2(nums: IntArray): List<List<Int>> {
        val answer = mutableListOf<List<Int>>()
        nums.sort()

        // 첫 세 수의 합이 0보다 크거나, 마지막 세 수의 합이 0보다 작으면 불가능
        val lastIndex = nums.size - 1
        if (nums[0] + nums[1] + nums[2] > 0 ||
            nums[lastIndex] + nums[lastIndex - 1] + nums[lastIndex - 2] < 0
        ) {
            return emptyList()
        }

        var prev = nums[0] - 1
        for (i in nums.indices) {
            // 조기 종료 조건 추가
            if (nums[i] > 0) {
                break
            }
            if (nums[i] == prev) {
                continue
            }
            var left = i + 1
            var right = nums.size - 1
            while (left < right) {
                // 중복 로직 제거 및 sum 변수화
                val sum = nums[i] + nums[left] + nums[right]
                when {
                    sum > 0 -> right = skipDuplicates(nums, right, false)
                    sum < 0 -> left = skipDuplicates(nums, left, true)
                    else -> {
                        answer.add(listOf(nums[i], nums[left], nums[right]))
                        left = skipDuplicates(nums, left, true)
                        right = skipDuplicates(nums, right, false)
                    }
                }
            }
            prev = nums[i]
        }
        return answer
    }

    private fun skipDuplicates(nums: IntArray, index: Int, isLeft: Boolean): Int {
        var current = index
        return if (isLeft) {
            while (current + 1 < nums.size && nums[current] == nums[current + 1]) current++
            current + 1
        } else {
            while (0 <= current - 1 && nums[current - 1] == nums[current]) current--
            current - 1
        }
    }

    @Test
    fun test() {
        threeSum(intArrayOf(-1, 0, 1, 2, -1, -4)) shouldBe listOf(
            listOf(-1, -1, 2),
            listOf(-1, 0, 1)
        )
        threeSum(intArrayOf(0, 1, 1)) shouldBe emptyList<Int>()
        threeSum(intArrayOf(0, 0, 0)) shouldBe listOf(
            listOf(0, 0, 0)
        )
        threeSum(intArrayOf(-2, 0, 0, 2, 2)) shouldBe listOf(
            listOf(-2, 0, 2)
        )
        threeSum2(intArrayOf(-1, 0, 1, 2, -1, -4)) shouldBe listOf(
            listOf(-1, -1, 2),
            listOf(-1, 0, 1)
        )
        threeSum2(intArrayOf(0, 1, 1)) shouldBe emptyList<Int>()
        threeSum2(intArrayOf(0, 0, 0)) shouldBe listOf(
            listOf(0, 0, 0)
        )
        threeSum2(intArrayOf(-2, 0, 0, 2, 2)) shouldBe listOf(
            listOf(-2, 0, 2)
        )
    }

}
