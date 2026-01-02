class Solution {
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val current = mutableListOf<Int>()

        fun dfs(start: Int, total: Int) {
            if (total > target) return

            if (total == target) {
                result.add(ArrayList(current))
                return
            }

            for (i in start until candidates.size) {
                val num = candidates[i]
                current.add(num)
                dfs(i, total + num)
                current.removeAt(current.size - 1)
            }
        }

        dfs(0, 0)
        return result
    }
}
