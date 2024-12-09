package leetcode_study

/**
 * 주어진 숫자들에서 빈도 수가 가장 큰 k 개의 숫자를 구하는 문제. map 자료구조를 사용해 해결
 * 시간 복잡도 : O(n)
 * -> Int Array를 순회해 map에 담는 과정 O(n)
 * -> 채워진 Map 자료구조에서 value 기준 내림차순으로 정렬 과정 O(nlogn)
 * -> 정렬된 Map에서 K 만큼 값을 가져오는 과정 O(K). (k는 상수)
 * 각 단계의 시간 복잡도를 더하면 : O(n) + O(nlogn) + O(k) -> O(nlogn)
 * 공간 복잡도 : O(n)
 * -> Int Array에 존재하는 유니크한 요소 만큼 필요함.
 */
fun topKFrequent(nums: IntArray, k: Int): IntArray {
    val map = mutableMapOf<Int, Int>()

    for (i in nums.indices) {
        if (map.containsKey(nums[i])) {
            val value = map[nums[i]]!!
            map[nums[i]] = value + 1
        } else {
            map.putIfAbsent(nums[i], 1)
        }
    }
    val sortedMap = map.toList().sortedByDescending { it.second }.toMap()
    return sortedMap.entries.take(k).map { it.key }.toIntArray()
}
