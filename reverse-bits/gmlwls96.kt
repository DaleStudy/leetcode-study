class Solution {
    // you need treat n as an unsigned value
    fun reverseBits(n: Int): Int {
        var bitString = Integer.toBinaryString(n)
        bitString = CharArray(32 - bitString.length) { '0' }.concatToString() + bitString
        var result = 0
        var scale = 1
        bitString.forEach {
            result += it.digitToInt() * scale
            scale *= 2
        }
        return result
    }
}
