package leetcode_study

fun productExceptSelf(nums: IntArray): IntArray {
    // ex. nums = [1, 2, 3, 4]
    val leftStartProducts = mutableListOf(1)
    val rightStartProducts = mutableListOf(1)

    // mutableNums = [1, 1, 2, 3, 4]
    val mutableNums = nums.toMutableList()
    mutableNums.add(0, 1)
    mutableNums.add(1)

    // leftStartProducts = [1, 1, 2, 6, 24, 24]
    // rightStartProducts = [24, 24, 24, 12, 4, 1]
    for (idx in 1..< mutableNums.size) {
        val leftNum = mutableNums[idx]
        val rightNum = mutableNums[mutableNums.size - 1 - idx]

        leftStartProducts.add(leftStartProducts.last() * leftNum)
        rightStartProducts.add(index = 0, element = rightStartProducts.first() * rightNum)
    }

    val result = mutableListOf<Int>()
    for (idx in 0..mutableNums.size - 3) {
        result.add(leftStartProducts[idx] * rightStartProducts[idx + 2])
    }

    return result.toIntArray()
}