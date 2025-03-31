/**
 * 배열에서 가장 작은 수 찾기 ( 제약 : 시간 복잡도 O(log n) )
 * @param {number[]} nums 회전된 수 배열
 * 
 * 시간 복잡되: O(log n)
 *  - 이분 탐색을 사용하여 최소값을 탐색
 * 
 * 공간 복잡도: O(1) 
 */
function findMin(nums: number[]): number {
    let left = 0, right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        // 정렬이 망가진 경우
        if (nums[mid] < nums[mid-1]) return nums[mid];

        // left, right 범위 줄여나가기
        if (nums[0] <  nums[mid]){
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
     
    // 탐색 후에도 찾지 못한 경우 회전되지 않은 경우
    return nums[0];

}

