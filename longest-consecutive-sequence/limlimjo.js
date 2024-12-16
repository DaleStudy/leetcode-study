/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    // 첫 번째 정렬을 한다.
    if (nums.length === 0) {
        return 0;
    }

    nums.sort((a, b) => a - b); // 오름차순으로 정렬
    console.log(nums);

    // 두 번째 숫자가 1씩 계속해서 증가하는 구간을 찾는다.
    let longest = 0;
    let length = 1;

    for (let i=0; i<nums.length-1; i++) {
        if (nums[i] === nums[i+1]) {
            continue;
        }
        // 연속해서 1씩 증가하는 구간 찾기
        if (nums[i+1] - nums[i] === 1) {
            length += 1;
        } else {
            longest = Math.max(longest, length);
            length = 1;
        }
    }
    return Math.max(longest, length);
};

// 시간복잡도와 공간복잡도
// 시간복잡도: 정렬 사용(O(nlogn)) + for문으로 배열 탐색(O(n)) = O(nlogn)
// 공간복잡도: O(1)
