class Solution {
    // 시간 : O(n), 공간 : O(n)
    // nums를 조회하면서 이전값과 비교하여
    // 더 증가하였으면  : 이전 카운트 +1
    // 같거나 작으면 : 이전 카운트값
    fun lengthOfLIS(nums: IntArray): Int {
        val count = IntArray(nums.size)
        count[0] = 1
        var prev = nums[0]
        for (i in 1 until nums.size) {
            if (prev < nums[i]) {
                count[i] += count[i - 1] + 1
            } else {
                count[i] = count[i - 1]
            }
            prev = nums[i]
        }
        return count.last()
    }
}
