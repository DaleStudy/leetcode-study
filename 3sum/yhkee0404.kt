class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        val ans = mutableListOf<List<Int>>()
        nums.sort()
        for (i in 0 until nums.size) {
            if (i != 0 && nums[i] == nums[i - 1]) {
                continue
            }
            var j = i + 1
            var k = nums.size - 1
            while (j < k) {
                if (j != i + 1 && nums[j] == nums[j - 1]) {
                    j++
                    continue
                }
                val u = nums[i] + nums[j]
                while (j < k && u > - nums[k]) {
                    k--
                }
                if (j >= k) {
                    break
                }
                if (u == - nums[k]) {
                    ans.add(listOf(nums[i], nums[j], nums[k]))
                }
                j++
            }
        }
        return ans
    }
}
