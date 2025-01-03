/**
 * @param {number[]} nums
 * @return {number[]}
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
var productExceptSelf = function(nums) {
  const answer = []
  const zeros = nums.filter(n => n === 0).length;
  if (zeros > 1) return new Array(nums.length).fill(0);
  
  const productOfNums = nums.reduce((acc, cur) => cur === 0 ? acc : acc * cur, 1);
  
  nums.forEach(num => {
    if (num === 0) {
      answer.push(productOfNums);
    } else {
      answer.push(zeros ? 0 : productOfNums / num);
    }
  });
  return answer
};

