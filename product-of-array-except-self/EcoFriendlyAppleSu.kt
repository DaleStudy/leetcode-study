package leetcode_study

/*
* 주어진 배열에서 자신 요소를 제외한 나머지 요소의 곱한 배열을 구하는 문제
* 문제에세 O(n)의 시간 복잡도를 요구하였으나 방법이 떠오르지 않아 고민 후 정답 참조.
* 기준 요소를 중심으로 왼쪽의 총 곱, 오른쪽의 총 곱을 진행하게 되었을 때, 문제를 O(n)의 시간 복잡도로 해결할 수 있음.
* 시간 복잡도: O(n^2)
* 공간 복잡도: O(n)
* */
fun productExceptSelf00(nums: IntArray): IntArray {
    val result = mutableListOf<Int>()

    for (i in nums.indices) {
        var temp = 1
        for (j in nums.indices) {
            if (i == j) continue
            temp *= nums[j]
        }
        result.add(temp)
    }
    return result.toIntArray()
}

/*
* 시간 복잡도: O(n)
* 공간 복잡도: O(n)
* */
fun productExceptSelf01(nums: IntArray): IntArray {
    val result = IntArray(nums.size)

    var leftProduct = 1
    for (i in nums.indices) {
        result[i] = leftProduct
        leftProduct = leftProduct * nums[i]
    }

    var rightProduct = 1
    for (i in nums.indices.reversed()) {
        result[i] = result[i] * rightProduct
        rightProduct = rightProduct * nums[i]
    }
    return result
}
