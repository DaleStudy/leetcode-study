/**
TC: O(32) = O(1)
SC: O(1)
 */
class Solution {
    fun reverseBits(n: Int): Int {
        var result = 0
        var num = n
        repeat(32) {
            result = (result shl 1) or (num and 1)
            num = num ushr 1
        }
        return result
    }
}
