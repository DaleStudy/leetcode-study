/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    //카데인 알고리즘
    let currentSum = nums[0] 
    let maxSum = nums[0] 
    for(let i = 1; i<nums.length;i++){
        currentSum = Math.max(nums[i],currentSum+nums[i])
        maxSum = Math.max(maxSum,currentSum)
    }
    
    return maxSum
};

//시간복잡도 : O(n)
//공간복잡도: O(1)
