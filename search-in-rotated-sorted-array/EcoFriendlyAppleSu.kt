package leetcode_study

/*
* 회전된(shifted) 정렬 배열에서 O(log n) 시간 복잡도로 target 값의 index를 찾는 문제
*
* 이진 탐색 (Binary Search) 사용
* 각 반복마다 중간 값(mid)을 기준으로 배열을 절반씩 줄이며 탐색
* 배열의 한쪽 절반은 항상 정렬되어 있으므로, 정렬된 구간을 기준으로 탐색 방향 결정
*
* 시간 복잡도: O(log n)
* -> 매번 탐색 공간을 절반으로 줄이므로 O(log n)
* 공간 복잡도: O(1)
* -> 추가적인 공간을 사용하지 않고 변수만 사용하므로 O(1)
* */
fun search(nums: IntArray, target: Int): Int {
    var start = 0
    var end = nums.size - 1

    while (start <= end) {
        val mid = start + (end - start) / 2
        if (nums[mid] == target) return mid

        // 왼쪽 부분이 정렬된 경우
        if (nums[start] <= nums[mid]) {
            if (nums[start] <= target && target < nums[mid]) {
                end = mid - 1  // 왼쪽에서 탐색
            } else {
                start = mid + 1 // 오른쪽에서 탐색 -> 다음 루프에서 정렬되지 않은 오른쪽 탐색
            }
        }
        // 오른쪽 부분이 정렬된 경우
        else {
            if (nums[mid] < target && target <= nums[end]) {
                start = mid + 1 // 오른쪽에서 탐색
            } else {
                end = mid - 1  // 왼쪽에서 탐색 -> 다음 루프에서 정렬되지 않은 왼쪽 탐색
            }
        }
    }
    return -1
}
