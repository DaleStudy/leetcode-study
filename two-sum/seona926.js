/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
let twoSum = function (nums, target) {
  let indices = {};

  nums.forEach((item, index) => {
    indices[item] = index;
  });

  for (let i = 0; i < nums.length; i++) {
    let findNum = target - nums[i];

    if (indices[findNum] !== i && findNum.toString() in indices) {
      return [indices[findNum], i];
    }
  }
};

/*
  1. 시간복잡도: O(n)
    - forEach와 for루프의 시간복잡도가 각 O(n)
  2. 공간복잡도: O(n)
    - indices 객체의 공간복잡도가 O(n), 나머지는 O(1)
*/
