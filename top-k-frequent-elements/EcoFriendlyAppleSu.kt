package leetcode_study

/**
 * 주어진 숫자들에서 빈도 수가 가장 큰 k 개의 숫자를 구하는 문제. map 자료구조를 사용해 해결
 * 시간 복잡도 : O(nlogn)
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

/**
 * 주어진 수의 빈도수를 기준으로 숫자를 할당하고 내림차순으로 순회해 k 개의 숫자를 얻게 되면 답을 도출하는 방법
 * 시간 복잡도 : O(n)
 * -> Int Array를 순회해 map에 담는 과정 O(n)
 * -> 빈도수 배열에 값을 채우는 과정 O(n)
 * -> 빈도수 배열을 내림차순으로 순회해 k 개를 만족하면 답을 도출하는 과정 O(n).
 * 이중 for loop 이지만 실제로는 빈도수가 유일한 숫자들만 고려되므로 k가 n보다 작거나 같은 경우에는 O(n)으로 가늠할 수 있음.
 * 각 단계의 시간 복잡도를 더하면 : O(n) + O(n) + O(n) -> O(n)
 * 공간 복잡도 : O(n)
 * -> Int Array에 존재하는 유니크한 요소 만큼 필요함.
 */
fun topKFrequent01(nums: IntArray, k: Int): IntArray {
    val map = mutableMapOf<Int, Int>()
    for(num in nums) {
        map[num] = map.getOrDefault(num, 0) + 1
    }

    // count List 초기화
    // map의 value는 nums Size를 넘을 수 없음.
    val countList = Array(nums.size + 1) { mutableListOf<Int>() }
    for ((key, value) in map) {
        countList[value].add(key)
    }

    val result = mutableListOf<Int>()
    for (i in countList.size - 1 downTo 0) {
        for (num in countList[i]) {
            result.add(num)
            if (result.size == k) {
                return result.toIntArray()
            }
        }
    }
    return result.toIntArray()
}
