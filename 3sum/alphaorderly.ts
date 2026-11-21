
/**
 * 시간 복잡도: O(n²)
 * 공간 복잡도: O(n)
 */
function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);

    let left = 0;
    let right = nums.length - 1;

    const ans: number[][] = [];

    while (left + 2 < nums.length) {
        if (nums[left] == nums[left - 1]) {
            left += 1;
            continue;
        }

        right = nums.length - 1;

        for (let mid = left + 1; mid < right;) {
            const sum = nums[left] + nums[mid] + nums[right];

            if (sum == 0) {
                ans.push([nums[left], nums[mid], nums[right]]);
                
                mid += 1;
                right -= 1;

                while (mid < right && nums[mid] == nums[mid - 1]) {
                    mid += 1;
                }
            } else if (sum < 0) {
                mid += 1;
            } else {
                right -= 1;
            }
        }

        left += 1;
    }

    return ans;
}
