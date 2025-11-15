// Runtime: 9ms / Memory: 60MB
function topKFrequent(nums: number[], k: number): number[] {
    const numFrequency:Record<number, number> = {}; // { n: freq }

    for (let i=0; i<nums.length; i++) {
        const n = nums[i];
        if (numFrequency[n]) numFrequency[n] = numFrequency[n] + 1;
        else numFrequency[n] = 1;
    }

    return Object.entries(numFrequency)
        .sort((a, b) => b[1] - a[1])
        .slice(0, k)
        .map(([_, n])=> n);
};