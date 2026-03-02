// TC: O(n)
// SC: O(n)
function twoSum(nums: number[], target: number): number[] {
    const n = nums.length;
    const complementMap = new Map<number, number>();

    for(let aIndex = 0; aIndex < n; aIndex++) {
        const a = nums[aIndex];
        const b = target - a;

        if(complementMap.has(b)) {
            return [complementMap.get(b) || -1, aIndex];
        }
        complementMap.set(a, aIndex);
    }

    return [-1, -1];
};
