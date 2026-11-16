// 시간복잡도 : O(n)
// 공간복잡도 : O(1)
function rob(nums: number[]): number {
    if (nums.length == 1) return nums[0];

    if (nums.length == 2) {
        return nums[0] > nums[1] ? nums[0] : nums[1];
    }

    let prev = nums[0];
    let current = nums[1];

    for (let i = 2; i < nums.length; i += 1) {
        let steal = prev + nums[i] > current ? prev + nums[i] : current;
        prev = prev > current ? prev : current;
        current = steal;
    }

    return current;
};
