/**
 * @param {number[]} nums
 * @return {boolean}
 */
 /*
    Goal: return true if duplicated #, false if no duplicated number

    Plan:
    - create a Set
    - loop num in nums
        - num exists in the Set -> return true
        - not exsits ->  add the num in the Set, continue to the next loop
    - return false 

    space complexity: O(n)
    time complexity: O(n)
  */
var containsDuplicate = function(nums) {
    const seen = new Set();

    for(const num of nums) {
        if (seen.has(num)) return true;
        seen.add(num);
    }
    return false; 
};
