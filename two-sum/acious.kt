class Solution {
    // nums의 모든 숫자를 Map에 저장. key는 nums의 숫자, value는 해당 숫자의 인덱스
    // target의 숫자가 동일한 숫자가 더해져야 하는 케이스 (예: target = 4, nums = [2, 2])를 위해 value는 List로 저장
    // 시간복잡도: O(n), 공간복잡도: O(n)
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, MutableList<Int>>()
        for (index in nums.indices) { // nums.indices는 nums의 인덱스 범위를 반환
            val list = map.getOrDefault(nums[index], mutableListOf())
            list.add(index)
            map[nums[index]] = list
        }
        for (index in nums.indices) {
            val complement = target - nums[index]
            val complementIndices = map[complement]
            if (complementIndices != null) {
                for (complementIndex in complementIndices) {
                    if (complementIndex != index) {
                        return intArrayOf(index, complementIndex)
                    }
                }
            }
        }
        throw IllegalArgumentException("No two sum solution")
    }
}