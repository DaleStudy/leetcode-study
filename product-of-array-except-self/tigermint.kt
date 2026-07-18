// class Solution {
//     fun productExceptSelf(nums: IntArray): IntArray {
//         val prefixProduct = IntArray(nums.size) { _ -> 1 }
//         val suffixProduct = IntArray(nums.size) { _ -> 1 }

//         for (i in 1 until nums.size) {
//            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]
//         }

//         for (i in nums.size - 2 downTo 0) {
//             suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1]
//         }

//         return IntArray(nums.size) { prefixProduct[it] * suffixProduct[it] }
//     }
// }

class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val answer = IntArray(nums.size) { _ -> 1 }

        for (i in 1 until nums.size) {
           answer[i] = answer[i - 1] * nums[i - 1]
        }

        var right = 1
        for (i in nums.size - 1 downTo 0) {
            answer[i] *= right
            right *= nums[i]
        }

        return answer
    }
}
