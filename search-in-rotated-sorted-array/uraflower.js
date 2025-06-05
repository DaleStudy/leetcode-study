/**
 * 주어진 배열에서 타겟의 인덱스를 찾아 반환하는 함수
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const search = function (nums, target) {
    let left = 0;
    let right = nums.length;
    let mid = Math.floor((left + right) / 2);

    while (left < right) {
        mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) break;
        
        // left부터 mid까지 잘 정렬되어 있는 경우 (=> rotate된 부분은 mid부터 right 사이에 있음)
        if (nums[left] < nums[mid]) {
            // 정렬된 left부터 mid 사이에 타겟이 있는 경우
            if (nums[left] <= target && target <= nums[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        // mid부터 right까지 잘 정렬되어 있는 경우 (=> rotate된 부분은 left부터 mid 사이에 있음)
        else {
            // 정렬된 mid부터 right 사이에 타겟이 있는 경우
            if (nums[mid] <= target && target <= nums[right - 1]) {
                left = mid;
            } else {
                right = mid;
            }
        }
    }

    return nums[mid] === target ? mid : -1;
};

// O(log n)
// O(1)
