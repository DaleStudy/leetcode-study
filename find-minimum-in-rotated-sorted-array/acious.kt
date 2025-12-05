class Solution {
    fun findMin(nums: IntArray): Int {
        var low = 1
        var high = nums.size - 1

        while (low <= high) {
            // 코틀린에서 Int끼리의 나눗셈은 자동으로 소수점을 버립니다 (Floor)
            val mid = (low + high) / 2

            // 회전된 지점(변곡점)을 찾은 경우: 바로 리턴
            if (nums[mid - 1] > nums[mid]) {
                return nums[mid]
            }

            // 왼쪽 부분이 정렬되어 있다면, 최소값은 오른쪽에 있음
            if (nums[0] < nums[mid]) {
                low = mid + 1
            } else {
                // 오른쪽 부분이 정렬되어 있다면(혹은 변곡점이 왼쪽에 있다면), 왼쪽으로 이동
                high = mid - 1
            }
        }

        // 반복문이 끝날 때까지 못 찾았거나, 배열이 회전되지 않은 경우 첫 번째 요소가 최소값
        return nums[0]
    }
}