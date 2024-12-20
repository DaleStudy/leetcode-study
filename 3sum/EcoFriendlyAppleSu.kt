package leetcode_study

/**
 * 주어진 배열의 세 원소의 합이 0인 경우를 구하는 문제. (세 개의 값의 결과는 중복되지 않음)
 *
 * 주어진 조건
 * 3 <= nums.length <= 3000
 * -105 <= nums[i] <= 105
 */

/**
 * case01. 조합을 사용한 풀이.
 * 시간 초과 발생 이유
 * -> 모든 가능한 세 개의 조합을 생성하기 때문에 발생.
 * 시간 복잡도:
 * -> 세 개의 조합 생성 과정: O(n * (n-1) * (n-2)) / 3. 최악의 경우 n = 3000, 4.5 억개 조합 생성
 * -> 세 개의 조합 결과 sorting 과정: O(klogk). k = 3
 * -> 결과값을 필터링해 합이 0인 배열을 필터하는 과정: O(n)
 * 나머지 연산이 세 개의 조합 생성 과정에 영향을 받아 계산 횟수 증가.
 *
 * 공간 복잡도:
 * -> 각 조합을 모두 저장: O(n^3)
 */
fun threeSumUseCombination(nums: IntArray): List<List<Int>> {
    // 결과를 담을 Set 자료구조
    val processResult = mutableSetOf<List<Int>>()

    // 주어진 배열의 크기를 담는 변수
    val maxNumber = nums.size

    // 조합 배열의 크기
    val givenSize = 3

    // 나타낼 인덱스를 구하는 배열 초기화
    val indices = IntArray(givenSize)
    for (i in 0 until givenSize) {
        indices[i] = i
    }

    while (indices[givenSize - 1] < maxNumber) {
        processResult.add(indices.map { nums[it] }.sorted())
        var i = givenSize - 1

        while (i >= 0 && indices[i] == i + maxNumber - givenSize) {
            i--
        }

        if (i >= 0) {
            indices[i]++
            for (j in i + 1 until givenSize) {
                indices[j] = indices[j-1] + 1
            }
        } else break
    }

    return processResult.filter { it.sum() == 0 }
}

/**
 * case02. 투 포인터를 사용한 풀이
 * 조합을 사용한 풀이와 달리 시간 초과가 발생하지 않음. O(n^3)의 시간 복잡도를 O(n^2)으로 줄임
 *
 * 시간 복잡도:
 * -> 주어진 숫자 배열 오름차순으로 정렬: O(nlogn)
 * -> 세 개의 숫자를 더하는 로직
 *      -> 외부 반복문을 통해 주어진 배열 전체 조회: O(n)
 *      -> 내부 반복문을 통해 start to last index 순회: O(n)
 *      -> O(n^2)
 * ∴ O(nlogn) + O(n^2) => O(n^2)
 *
 * 공간 복잡도:
 * -> 주어진 숫자 배열의 정렬을 담는 공간 필요: O(n)
 */
fun threeSum(nums: IntArray): List<List<Int>> {
    val processResult = mutableListOf<List<Int>>()
    val sortedNums = nums.sorted()

    for (i in sortedNums.indices) {
        if (i > 0 && sortedNums[i] == sortedNums[i-1]) continue

        var startIndex = i + 1
        var lastIndex = sortedNums.size - 1

        while (startIndex < lastIndex) {
            val sum = sortedNums[i] + sortedNums[startIndex] + sortedNums[lastIndex]
            when {
                sum == 0 -> {
                    processResult.add(listOf(sortedNums[i], sortedNums[startIndex], sortedNums[lastIndex]))
                    while (startIndex < lastIndex && sortedNums[startIndex] == sortedNums[startIndex + 1]) startIndex++
                    while (startIndex < lastIndex && sortedNums[lastIndex] == sortedNums[lastIndex - 1]) lastIndex--
                    startIndex++
                    lastIndex--
                }
                sum < 0 -> {
                    startIndex++
                }
                else -> {
                    lastIndex--
                }
            }
        }
    }
    return processResult
}
