class Solution {
    // 시간복잡도 : O(n) : map 세팅, O(nlogn) : map value 정렬 = O(nlogn)
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val map = mutableMapOf<Int, Int>()

        for (num in nums) {
            // 더 효율적이고 가독성 좋은 getOrDefault 사용
            map[num] = map.getOrDefault(num, 0) + 1
        }

        // 1. value를 기준으로 내림차순 정렬 후 key만 추출
        val sortedKeys = map.entries
            .sortedByDescending { it.value }
            .map { it.key }

        // 2. 0부터 k개(0 until k)를 자르고 IntArray로 변환
        return sortedKeys.slice(0 until k).toIntArray()
    }
}