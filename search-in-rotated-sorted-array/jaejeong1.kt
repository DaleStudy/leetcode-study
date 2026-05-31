class `Search-in-Rotated-Sorted-Array` {
    fun search(nums: IntArray, target: Int): Int {
        // log n -> 이진 탐색
        // 이진 탐색 -> 왼쪽은 작고, 오른쪽은 크다
        // 그렇다면.. 회전된 인덱스 기준으로 잘라서 좌우에서 각각 이진 탐색하면 가능하다
        // 회전된 인덱스 어떻게 찾나? -> 이진 탐색해서 좌측이 더 크거나, 우측이 더 작으면 우측이 인덱스다

        // 1단계: 이진 탐색해서 회전한 인덱스 찾기
        // 2단계: 회전한 인덱스 기준으로 좌우 자르고, 각각 이진 탐색하기
        // 3단계: 둘다 없으면 -1, 좌측 또는 우측에서 답 찾아서 반환
        // 시간복잡도: O(log n), 공간복잡도: O(1)

        val rotatedIndex = findRotatedIndex(nums)
        val index = binarySearch(nums, 0, rotatedIndex - 1, target)
        // 왼쪽에 답이 있는지
        if (index > -1) {
            return index
        }
        // 없으면 오른쪽 답 탐색해서 반환
        return binarySearch(nums, rotatedIndex, nums.size - 1, target)
    }

    fun findRotatedIndex(nums: IntArray): Int {
        // nums[0] 이 nums[mid]보다 크면 rotated index 는 왼쪽에 있음
        // 정렬되어있다면 위 조건이 될 수 없기 때문
        var left = 0
        var right = nums.size - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            // 좌측 값이 더 크면 rotated index
            if (0 < mid && nums[mid - 1] > nums[mid]) {
                return mid
            }
            // 왼쪽이 정렬되었는지
            if (nums[0] <= nums[mid]) {
                left = mid + 1
            }
            // 오른쪽이 정렬되었는지
            else {
                right = mid - 1
            }
        }
        return 0
    }

    fun binarySearch(nums: IntArray, left: Int, right: Int, target: Int): Int {
        var left = left
        var right = right

        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums[mid] == target) {
                return mid
            }
            if (nums[mid] < target) {
                left = mid + 1
            }
            else {
                right = mid - 1
            }
        }
        return -1
    }
}
