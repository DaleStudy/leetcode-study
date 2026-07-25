class Solution {
    fun findMin(nums: IntArray): Int {
        var left = 0
        var right = nums.size - 1

        while (left < right) {
            val mid = (left + right) / 2

            when {
                nums[mid] > nums[right] -> left = mid + 1 // 오른쪽 존재
                nums[mid] <= nums[right] -> right = mid // 왼쪽 존재 or 나 자신
            }
        }

        return nums[left]
    }
}
