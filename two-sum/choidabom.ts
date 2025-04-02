// https://leetcode.com/problems/two-sum/

// TC: O(n^2)
// SC: O(1)

function twoSum(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length; i++) {
      for (let j = i + 1; j < nums.length; j++){
        if (nums[i] + nums[j] === target){
          return [i, j]
        }
      }
    }
    return []
};

// TC: O(n)
// SC: O(n)

function twoSum(nums: number[], target: number): number[] {
    const map = new Map()

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i]
        const diff = target - num

        if (map.has(diff)) {
            return [i, map.get(diff)]
        } else {
            map.set(num, i)
        }
    }
    return []
};

console.log(twoSum([2,7,11,15], 9))