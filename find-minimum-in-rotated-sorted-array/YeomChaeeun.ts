/**
 * 정렬된 배열에서 최소값 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(logn)
 * - 공간 복잡도: O(1)
 * @param nums
 */
function findMin(nums: number[]): number {
    // 풀이 1 - sort() 사용
    // 시간 복잡도: O(nlogn) / 공간 복잡도: O(1)
    // nums.sort((a, b) => a - b)
    // return nums[0]

    // 풀이 2 - 배열이 정렬되어 있음을 활용한 풀이
    // 시간 복잡도: O(n) / 공간 복잡도: O(1)
    // let min = nums[0];
    // for(let i = 1; i < nums.length; i++) {
    //     console.log(nums[i])
    //     min = Math.min(nums[i], min)
    // }
    // return min

    // 이분 탐색법 활용
    // 절반씩 잘라서 nums[n-1] > nums[n] 의 지점을 찾는다
    let low = 1;
    let high = nums.length - 1;
    while(low <= high) {
        let mid = Math.floor((low + high) / 2);
        if(nums[mid - 1] > nums[mid]) {
            return nums[mid];
        }
        if(nums[0] < nums[mid]) {
            low = mid + 1;
        } else {
            high = mid -1;
        }
    }
    return nums[0]
}
