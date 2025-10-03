object Solution {
    def missingNumber(nums: Array[Int]): Int = {
        (1 to nums.length).reduce(_ ^ _) ^ nums.reduce(_ ^ _) // T(n) = O(n), S(n) = O(1)
    }
}
