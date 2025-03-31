// similar problem to #245 Find Minimum In Rotated Sorted Array
/**
 * 회정된 배열에서 target의 index를 찾는 문제
 * @param {number[]} nums - 회전된 배열
 * @param target - 찾는 수
 * @returns {number} - target의 index
 * 
 * 시간 복잡도: O(log n)
 *  - 이분 탐색을 사용하여 최적의 탐색을 수행
 * 
 * 공간 복잡도: O(1)
 *  - 추가적인 공간 사용 없이 포인터만 이용하여 탐색
 */
function search(nums: number[], target: number): number {
    let left = 0, right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) return mid;

        // mid를 기준으로 왼쪽 부분이 정렬된 경우
        if (nums[left] <= nums[mid]) {
            /**
             * 왼쪽 부분이 오름차순 정렬되어 있다면:
             * - nums[left] ~ nums[mid] 범위는 정렬되어 있음
             * - target이 이 범위 내에 있다면, right를 줄여서 탐색
             * - 아니라면 target은 오른쪽에 있으므로 left를 증가시켜 탐색
             */
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1; // 왼쪽 범위에서 탐색
            } else {
                left = mid + 1; // 오른쪽 범위에서 탐색
            }
        } 
        // mid를 기준으로 오른쪽 부분이 정렬된 경우
        else {
            /**
             * 오른쪽 부분이 오름차순 정렬되어 있다면:
             * - nums[mid] ~ nums[right] 범위는 정렬되어 있음
             * - target이 이 범위 내에 있다면, left를 늘려서 탐색
             * - 아니라면 target은 왼쪽에 있으므로 right를 감소시켜 탐색
             */
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1; // 오른쪽 범위에서 탐색
            } else {
                right = mid - 1; // 왼쪽 범위에서 탐색
            }
        }
    }

    // target을 찾지 못한 경우
    return -1;
}

