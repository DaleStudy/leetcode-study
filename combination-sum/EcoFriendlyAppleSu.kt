package leetcode_study

/*
* target을 구성할 수 있는 모든 조합의 수를 구하는 문제
* 재귀를 사용해 모든 경우의 수를 구한 후 구한 결과값에서 중복을 제거하는 방식으로 문제 해결
* 시간 복잡도: O(2^(target size))
* -> target 값을 0으로 만들기 위해 가능한 모든 조합을 찾는 과정
* 공간 복잡도: O(2^(target size))
* -> removeDuplicates는 중복을 제거하고 결과를 저장하는 데 사용됨. 중복을 제외하는 과정에서 O(2^(target size))개의 리스트 사용
* */
fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
    val result = mutableListOf<List<Int>>()

    fun combination(target: Int, current: List<Int>) {
        if (target == 0) {
            result.add(current)
            return
        }
        if (target < 0) return

        for (candidate in candidates) {
            combination(target - candidate, current + candidate)
        }
    }
    combination(target, emptyList())

    val removeDuplicates = mutableSetOf<List<Int>>()

    for (i in result) {
        val temp = i.sorted()
        removeDuplicates.add(temp)
    }
    return removeDuplicates.toList()
}

/*
* 재귀를 사용하여 문제를 해결할 때, 재귀 작성 시 중복을 제거하는 방식으로 문제 해결
* 시간 복잡도: O(2^(target size))
* -> target 값을 0으로 만들기 위해 가능한 모든 조합을 찾는 과정
* 공간 복잡도: O(target size)
* -> 재귀 호출 스택에서 사용하는 공간이 target 값에 비례하기 때문에, 재귀 깊이는 O(target size)
* */
fun combinationSumUsingBackTracking(candidates: IntArray, target: Int): List<List<Int>> {
    val result = mutableListOf<List<Int>>()

    fun combination(target: Int, current: MutableList<Int>, start: Int) {
        if (target == 0) {
            result.add(current.toList()) // 현재 조합을 결과에 추가
            return
        }
        if (target < 0) return

        for (i in start until candidates.size) {
            current.add(candidates[i]) // 후보 추가
            combination(target - candidates[i], current, i) // 현재 후보를 다시 사용할 수 있음
            current.removeAt(current.lastIndex) // 백트래킹
        }
    }

    combination(target, mutableListOf(), 0)
    return result
}
