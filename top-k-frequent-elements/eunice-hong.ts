
/**
 * Finds the k most frequent elements in an array.
 * Uses a map to count occurrences and then sorts by frequency.
 *
 * @param nums - An array of integers.
 * @param k - The number of most frequent elements to return.
 * @returns An array of the k most frequent elements.
 *
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 */
function topKFrequent(nums: number[], k: number): number[] {
    let numMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        numMap.set(nums[i], (numMap.get(nums[i]) ?? 0) + 1);
    }
  
    return Array.from(numMap.entries())
        .sort((a, b) => b[1] - a[1]) 
        .slice(0, k)
        .map(([num, _]) => num);
};
