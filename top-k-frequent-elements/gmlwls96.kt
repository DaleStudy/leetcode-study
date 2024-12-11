class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val answer = IntArray(k)
        val set = nums.toSet()
        val mutableList = mutableListOf<Pair<Int, Int>>()
        set.forEach { num ->
            mutableList.add(num to nums.count { it == num })
        }
        mutableList.sortByDescending { it.second }
        for (i in 0 until k) {
            answer[i] = mutableList[i].first
        }
        return answer
    }
}
