package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `search-in-rotated-sorted-array` {

    /**
     * O(log n)만큼의 시간만으로 해결해야 한다.
     * nums 배열은 정렬되어있지만 순환된 배열이므로 target 을 찾기 위한 일반적인 이분 탐색으로는 해결할 수 없다.
     * TC: O(log n), SC: O(1)
     */
    fun search(nums: IntArray, target: Int): Int {
        var (low, high) = 0 to nums.size - 1

        while (low + 1 < high) {
            val mid = (low + high) / 2

            if (nums[mid] == target) {
                return mid
            }
            if (nums[low] <= nums[mid]) {
                if (target in nums[low] .. nums[mid]) {
                    high = mid
                } else {
                    low = mid
                }
            } else {
                if (target in nums[mid] .. nums[high]) {
                    low = mid
                } else {
                    high = mid
                }
            }
        }
        return when (target) {
            nums[low] -> low
            nums[high] -> high
            else -> -1
        }
    }

    @Test
    fun `배열에서 타겟의 인덱스를 반환한다`() {
        search(intArrayOf(4,5,6,7,0,1,2), 0) shouldBe 4
        search(intArrayOf(4,5,6,7,0,1,2), 3) shouldBe -1
        search(intArrayOf(2,3,4,5,6,0,1), 1) shouldBe 6
        search(intArrayOf(1,2,3,4,5,6,7), 6) shouldBe 5
    }
}
