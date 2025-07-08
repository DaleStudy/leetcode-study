class Solution {
    /*
    0 -> 0
    1 -> 1
    2 -> 1
    3 -> 2
    4 -> 1
    5 -> 2
    6 -> 2
    7 -> 3
    8 -> 1
    9 -> 2
    10 -> 2
    11 -> 3
    12 -> 2
    2,4,8,16,.. -> 1
    짝수: i/2의 1의 개수
    홀수: i/2의 1의 개수 + 1
     */
    // TC: O(n)
    // SC: O(n)
    fun countBits(n: Int): IntArray {
        val result = IntArray(n + 1)
        for(i in 0..n) {
            result[i] = result[i / 2] + (i % 2)
        }
        return result
    }
}
