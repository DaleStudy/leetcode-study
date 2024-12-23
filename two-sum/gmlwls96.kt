class Solution {
    // 시간 : O(NlogN)-정렬하는데 드는 시간복잡도., 공간(2N)
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val sortNums = List(nums.size) { listOf(nums[it], it) }.sortedBy { it[0] }
        // 1. list( list('값', 'index')) 형태의 list를 만들고 값을 기준으로 정렬한다.

        var i = 0
        var j = sortNums.lastIndex
        // 2. 2포인터 방식으로 두 값을 합했을때 target이 되는 값을 찾는다.
        while (i < j) {
            val sum = sortNums[i][0] + sortNums[j][0]
            when {
                sum == target -> { // target과 sum이 일치할시 바로 return.
                    return intArrayOf(
                        min(sortNums[i][1], sortNums[j][1]),
                        max(sortNums[i][1], sortNums[j][1])
                    )
                }
                sum < target -> { // sum이 target보다 값이 작은경우 i를 한칸씩 더한다.
                    i++
                }
                sum > target -> { // sum이 target보다 값이 큰경우 j를 한칸씩 내린다.
                    j--
                }
            }
        }
        return intArrayOf()
    }
}
