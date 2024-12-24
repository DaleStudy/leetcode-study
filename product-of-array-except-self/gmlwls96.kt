class Solution {
    // 시간 : O(2n) = O(n) ,공간 : O(1)
    fun productExceptSelf(nums: IntArray): IntArray {
        val answer = IntArray(nums.size) { 1 }

        var n = 1
        for (i in 0 until nums.lastIndex) {
            n *= nums[i]
            answer[i + 1] = n
        }
        println(answer.toList())

        n = 1
        for (i in nums.lastIndex downTo 1) {
            n *= nums[i]
            answer[i - 1] *= n
        }
        return answer
    }
}
