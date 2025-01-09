package leetcode_study

/**
 * 주어진 숫자 배열에서 두 개의 숫자를 더해 Target을 만들 수 있는 배열의 Index를 구하는 문제
 * 조합을 사용해 문제 해결
 * 시간 복잡도: O(n^2)
 * -> 두 번의 순회를 통해 모든 경우의 수를 계산하는 경우
 * 공간 복잡도: O(1)
 * -> 결과를 저장하는 result, 배열의 index를 가리키는 indices는 두 개의 값을 담기 때문에 O(1)
 */
fun twoSum(nums: IntArray, target: Int): IntArray {
    val result = IntArray(2)
    val k = 2
    val maxSize = nums.size
    val indices = IntArray(k)
    for (i in 0 until k ) {
        indices[i] = i
    }

    while (indices[k-1] < maxSize) {
        if (nums[indices[0]] + nums[indices[1]] == target) {
            result[0] = indices[0]
            result[1] = indices[1]
            return result
        }

        var i = k - 1
        while (i >= 0 && indices[i] == i + maxSize - k) {
            i--
        }

        if (i >= 0) {
            indices[i]++
            for (j in i + 1 until k) {
                indices[j] = indices[j - 1] + 1
            }
        } else {
            break
        }
    }
    return result
}
