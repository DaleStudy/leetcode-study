// Time Complexity: O(n)
// Space Complexity: O(m)

var topKFrequent = function(nums, k) {
    const frequencyMap = new Map();
    // for each number in the array, update frequency.
    for (const num of nums) {
        frequencyMap.set(num, (frequencyMap.get(num) || 0));
    }

    // create buckets where index represents frequency.
    const buckets = Array(nums.length + 1).fill().map(() => []);
    // place each number into the bucket corresponding to frequency.
    for (const [num, frequency] of frequencyMap.entries()) {
        buckets[frequency].push(num);
    }

    const result = [];
    // iterate from the highest possible frequency down to the lowest.
    for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
        if (buckets[i].length > 0) {
            result.push(...buckets[i]);
        }
    }

    // ensure the result length is k.
    return result.slice(0, k); 
};
