// Time Complexity: O(n^2)
// Space Complexity: O(n)

// Time Complexity: O(n^2)
// Space Complexity: O(n)

var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    // create a set to store triplets.
    const result = new Set();

    // loop through the array, but stop 2 elements before the end.
    for (let i = 0; i < nums.length - 2; i++) {
        // if the current element is the same as the one before it, skip it to avoid duplicates.
        if (i > 0 && nums[i] === nums[i - 1]) continue;
    
        // create a set to keep track of the complements.
        const complements = new Set();
        // start another loop from the next element.
        for (let j = i + 1; j < nums.length; j++) {
            const complement = -nums[i] - nums[j];
            // check if the current number is in the set.
            if (complements.has(nums[j])) {
                // if it is, found a triplet. Add it to the result set as a sorted string to avoid duplicates.
                result.add(JSON.stringify([nums[i], complement, nums[j]].sort((a, b) => a - b)));
            } else {
                complements.add(complement);
            }
        }
    }

    // convert set of strings back to arrays.
    return Array.from(result).map(triplet => JSON.parse(triplet));
};
