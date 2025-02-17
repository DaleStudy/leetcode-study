/**
 * 정렬된 배열에 target 문자의 인덱스 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(logn)
 * - 공간 복잡도: O(1)
 * @param nums
 * @param target
 */
function search(nums: number[], target: number): number {
    // findIndex 는 시간복잡도 O(n) 임
    // return nums.findIndex(value => value === target)?? -1

    // 정렬되어 있는 특성을 이용한 풀이
    let low = 0;
    let high = nums.length - 1;
    while(low <= high) {
        let mid = low + Math.floor((high - low) / 2);

        if(nums[mid] === target) return mid

        if(nums[low] <= nums[mid]) {
            if(nums[low] <= target && target < nums[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else {
            if(nums[mid] < target && target <= nums[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

    }

    return -1
}
