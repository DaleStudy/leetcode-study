class Solution {
    // 시간 : O(logN) 공간 : O(1)
    // 이분탐색.
    fun findMin(nums: IntArray): Int {
        var left = 0
        var right = nums.lastIndex

        while (left <= right){
            val mid = (left + right)/2
            when{
                nums[mid-1] > nums[mid] -> {
                    return nums[mid]
                }
                nums[0] < nums[mid] -> {
                    left = mid + 1
                }
                else -> {
                    right = mid -1
                }
            }
        }
        return nums[0]
    }
}
