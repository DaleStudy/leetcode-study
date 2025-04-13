/**
 * [Problem]: [15] 3Sum
 * (https://leetcode.com/problems/3sum/description/)
 */

function threeSum(nums: number[]): number[][] {
    //시간 복잡도: O(n^2)
    //공간 복잡도: O(1)
    function pointerFunc(nums: number[]): number[][] {
        const result: number[][] = [];
        nums.sort((a, b) => a - b);

        for (let i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) continue;
            let left = i + 1;
            let right = nums.length - 1;

            while (left < right) {
                const sum = nums[i] + nums[left] + nums[right];
                if (sum === 0) {
                    result.push([nums[i], nums[left], nums[right]]);

                    while (left < right && nums[left] === nums[left + 1]) left++;
                    while (left < right && nums[right] === nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return result;
    }

    return pointerFunc(nums);
}
