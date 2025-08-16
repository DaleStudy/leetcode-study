// 시간 복잡도: O(log n)
//   - n: 배열의 길이
//   - 매 반복마다 탐색 범위를 절반으로 줄이는 이진 탐색이므로 O(log n)
//
// 공간 복잡도: O(1)
//   - 추가적인 배열이나 자료구조를 사용하지 않고,
//     변수(left, right, mid)만 사용하므로 상수 공간

class Solution {
    fun findMin(nums: IntArray): Int {
        var left = 0
        var right = nums.size - 1

        while (left < right) {
            val mid = left + (right - left) / 2

            if (nums[mid] > nums[right]) {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return nums[left]
    }
}
