/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
  if(nums.length === 0) return 0;

  const numSet = new Set(nums);
  let longest = 0;

  for (const num of numSet) {
    if(!numSet.has(num-1)) {
      let currentNum = num;
      let currentLength = 1;

      while(numSet.has(currentNum+1)) {
        currentNum++;
        currentLength++;
      }

      longest = Math.max(longest, currentLength)
    }
  }
  return longest;
};