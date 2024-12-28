package leetcode_study

fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    val nums = ArrayDeque<Int>()
    dfs(candidates, target, 0, 0, nums, result)

    return result
}

private fun dfs(candidates: IntArray, target: Int, startIdx: Int, total: Int, nums: ArrayDeque<Int>, result: MutableList<List<Int>>) {
    if (target < total) return
    if (target == total) {
        result.add(ArrayList(nums))
        return
    }
    for (i in startIdx..< candidates.size) {
        val num = candidates[i]
        nums.add(num)
        dfs(candidates, target, i, total + num, nums, result)
        nums.removeLast()
    }
}
