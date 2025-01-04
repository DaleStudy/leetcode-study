class Solution {
    fun missingNumber(nums: IntArray): Int {
        nums.sort()
        var num = nums[0]
        for (i in 1 until nums.size) {
            if (nums[i] != (num + 1)) {
                return num + 1
            }
            num = nums[i]
        }
        return num + 1
    }
}
