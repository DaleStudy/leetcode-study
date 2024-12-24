class Solution {
    // 시간 : O(c^t), 공간 : O(t)
    // 알고리즘 : dfs
    val answerList = mutableSetOf<List<Int>>()

    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        candidates.sort()
        combination(
            candidates = candidates,
            target = target,
            current = 0,
            currentList = listOf()
        )
        return answerList.toList()
    }

    private fun combination(
        candidates: IntArray,
        target: Int,
        current: Int,
        currentList: List<Int>
    ) {
        candidates.forEach { // candidates를 한개씩 꺼내
            val sum = current + it // 현재값을 더했을때
            when {
                sum == target -> { // sum이 target과 동일한 값이면 answer 에 추가.
                    answerList.add(
                        currentList.toMutableList().apply {
                            add(it)
                            sort()
                        }
                    )
                }

                sum < target -> { // sum이 모자르면 다른 조합을 찾기 위해 재귀 호출.
                    combination(
                        candidates = candidates,
                        target = target,
                        current = sum,
                        currentList = currentList.toMutableList().apply {
                            add(it)
                        }
                    )
                }

                else -> return
            }
        }
    }
}
