class Solution {
    // 시간 복잡도 : O(n^2)
    fun threeSum(nums: IntArray): List<List<Int>> {
        val mutableSet = mutableSetOf<List<Int>>() // 결과를 담기 위한 set. 중복을 없애야되서 set으로 만듬.
        nums.sort() // 1. nums array를 정렬해주고
        for (i in 0..nums.size - 3) {
            for (j in i + 1..nums.size - 2) {
                for (k in j + 1..nums.lastIndex) {
                    // 2. nums의 3숫자를 뽑아내기 위해 i, j, k를 순차적으로 조회하면서 합했을때 0이 되는지 체크.
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        mutableSet.add(listOf(nums[i], nums[j], nums[k]))
                    }
                }
            }
        }
        return mutableSet.toList() // 3. 최종적으로 뽑아낸 결과를 return값에 맞게 set > list로 변환.
    }
}
