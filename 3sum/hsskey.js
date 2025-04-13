/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const result = [];
    const n = nums.length;
    
    if (n < 3) return result;
    
    nums.sort((a, b) => a - b);
    
    const uniqueTriplets = new Set();
    
    for (let i = 0; i < n - 2; i++) {
        if (nums[i] > 0) break;
        
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        const target = -nums[i];
        const seen = new Set();
        
        for (let j = i + 1; j < n; j++) {
            const complement = target - nums[j];
            
            if (seen.has(complement)) {
                const triplet = [nums[i], complement, nums[j]].toString();
                
                if (!uniqueTriplets.has(triplet)) {
                    uniqueTriplets.add(triplet);
                    result.push([nums[i], complement, nums[j]]);
                }
            }
            
            seen.add(nums[j]);
        }
    }
    
    return result;
};
