object Solution {
    def findMin(nums: Array[Int]): Int = {
        var l = 0
        var r = nums.size
        while (l != r) {
            val m = l + ((r - l) >> 1)
            // T(n) = lg(n)
            if (nums(m) <= nums.last) {
                r = m
            } else {
                l = m + 1
            }
        }
        nums(l)
    }
}
