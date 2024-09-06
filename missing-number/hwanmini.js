// 시간복잡도 O(n log n)
// 공간복잡도 O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    nums.sort((a,b) => a - b);

    for (let i = 0 ; i <= nums.length; i++) {
        if (i !== nums[i]) return i
    }

};

console.log(missingNumber([3, 0, 1]))
console.log(missingNumber([0, 1]))
console.log(missingNumber([9,6,4,2,3,5,7,0,1]))
