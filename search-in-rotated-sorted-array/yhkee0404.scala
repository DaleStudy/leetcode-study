object Solution {
    def search(nums: Array[Int], target: Int): Int = {
        var l = 0
        var r = nums.length - 1
        while (l != r) {
            val mid = r - ((r - l) >> 1)
            if (nums(mid) > nums(0)) {
                l = mid
            } else {
                r = mid - 1
            }
        }
        l = r + 1
        r = l + nums.length
        while (l != r) {
            val mid = l + ((r - l) >> 1)
            if (nums(mid % nums.length) < target) {
                l = mid + 1
            } else {
                r = mid
            }
        }
        l %= nums.length
        if (nums(l) == target) l else -1
    }
}
