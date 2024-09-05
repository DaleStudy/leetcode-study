/**
 * @param {number[]} nums
 * @return {number[]}
 */

/**
 * Runtime: 124ms, Memory: 65.06MB
 * Time complexity: O(n^2)
 * Space complexity: O(n)
 * -> answer 배열에 O(n)
 * -> splicedArr 배열에 O(n)
 */

var productExceptSelf = function (nums) {
  const totalProduct = nums.reduce((total, current) => total * current, 1);
  const answer = Array(nums.length).fill(0);

  for (let i = 0; i < nums.length; i++) {
    answer[i] = totalProduct / nums[i];
    if (nums[i] === 0) {
      const splicedArr = nums.filter(function (_, index) {
        return index !== i;
      });
      answer[i] = splicedArr.reduce((total, current) => total * current, 1);
    }
  }

  return answer;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */

/**
 * 위의 풀이는 0일 때마다 순회를 해야 하기 때문에 해당 부분을 0의 개수를 세어 처리하도록 변경한 풀이

 * Runtime: 109ms, Memory: 63.45MB
 * Time complexity: O(n)
 * Space complexity: O(n)

 */
var productExceptSelf = function (nums) {
  let totalProduct = 1;
  let zeroCount = 0;
  const answer = Array(nums.length).fill(0);

  for (let numIndex = 0; numIndex < nums.length; numIndex++) {
    if (nums[numIndex] === 0) {
      zeroCount += 1;
    } else {
      totalProduct *= nums[numIndex];
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      if (zeroCount - 1 > 0) {
        answer[i] = 0;
      } else {
        answer[i] = totalProduct;
      }
    } else {
      if (zeroCount > 0) {
        answer[i] = 0;
      } else {
        answer[i] = totalProduct / nums[i];
      }
    }
  }

  return answer;
};
