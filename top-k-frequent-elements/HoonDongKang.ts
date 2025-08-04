/**
 * [Problem]: [347] Top K Frequent Elements
 * (https://leetcode.com/problems/top-k-frequent-elements/description/)
 */

function topKFrequent(nums: number[], k: number): number[] {
    // 시간복잡도 O(nlogn)
    // 공간복잡도 O(n)
    function mapFun(nums: number[], k: number): number[] {
        const frequentMap = new Map<number, number>();

        for (let i = 0; i < nums.length; i++) {
            frequentMap.set(nums[i], (frequentMap.get(nums[i]) || 0) + 1);
        }

        const sorted = Array.from(frequentMap.entries()).sort((a, b) => b[1] - a[1]);

        return sorted.slice(0, k).map(([num]) => num);
    }

    return mapFun(nums, k);
}
