/*
    Goal: return indices of the two numbers such that they add up to target

    Plan:
    - create a hash map (dict) to store number -> index
    - loop through nums with index i
        - get currentNum = nums[i]
        - compute pairNum = target - currentNum
        - if pairNum exists in dict
            -> return [dict[pairNum], i]
        - otherwise store currentNum in dict with its index
    - if no pair is found, return [-1, -1]

    space complexity: O(n)
    time complexity: O(n)
*/

var twoSum = function(nums, target) {
    const dict = {};

    for (let i = 0; i < nums.length; i++) {
        const currentNum = nums[i];
        const pairNum = target - currentNum;

        if (typeof dict[pairNum] === 'number') {
            return [dict[pairNum], i];
        } else {
            dict[currentNum] = i;
        }
    }

    return [-1, -1];
};
