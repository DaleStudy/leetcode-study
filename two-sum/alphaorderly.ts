// 시간복잡도 : O(n)
// 공간복잡도 : O(n)
function twoSum(nums: number[], target: number): number[] {
    const map = new Map<number, number>();

    for (let index = 0; index < nums.length; index += 1) {
        if (map.has(nums[index])) {
            return [map.get(nums[index]), index];
        }

        map.set(target - nums[index], index);
    }

    return [];
};
