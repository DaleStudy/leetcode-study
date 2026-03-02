class Solution {
    // 1 <= nums.length <= 10^5
    // Integer.MIN_VALUE(2,147,483,647) < -10^9 <= nums[i] <= 10^9 < Integer.MAX_VALUE(2,147,483,647)
    // HashSet에 아이템을 하나씩 넣으면서 이미 존재하는 아이템이 있으면 true, 없으면 false
    // 시간복잡도 : O(n), 공간복잡도 : O(n)
    fun containsDuplicate(nums: IntArray): Boolean {
        val set = HashSet<Int>()
        for (num in nums) {
            if (set.contains(num)) {
                return true
            }
            set.add(num)
        }
        return false
    }
}