class Solution {
    // 배열에서 연속된 숫자의 개수를 구하는 문제
    // 1. 중복은 제거하고 카운트
    // 2. 정렬하지 않고 계산도 가능
    fun longestConsecutive(nums: IntArray): Int {
        if(nums.isEmpty()) return 0

        val numSet = nums.toHashSet()
        var maxLen = 0

        for(num in nums){
            if((num - 1) !in numSet){
                var currNum = num
                var currLen = 1

                while((currNum + 1) in numSet){
                    currNum++
                    currLen++
                }
                if(currLen > maxLen) maxLen = currLen
            }
        }
        return maxLen
    }
}

