/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/**
 * Runtime: 107ms, Memory: 49.52MB
 * Time complexity: O(n^2)
 * Space complexity: O(n^2)
 *
 * **/

var twoSum = function (nums, target) {
  const answer = [];
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/**
 * 다른 풀이: two의 sum 이니까 target - 현재 값을 한 뒤, 나머지 값이 배열에 있는지 찾는 방법.
 * 이 과정에서 해시맵을 사용해서 target - 현재 값이 map 에 존재하면 return
 * 없다면 map에 나머지 값과 그에 해당하는 인덱스를 추가한다.
 * 그럼 추후에는 나머지 값을 map에서 O(1)로 찾기만 하면 된다.
 *
 * Runtime: 49ms, Memory: 49.52MB
 * Time complexity: O(n)
 * Space complexity: O(n)
 * **/

var twoSum = function (nums, target) {
  let map = new Map();

  for (i = 0; i < nums.length; i++) {
    if (map.has(target - nums[i])) return [map.get(target - nums[i]), i];
    map.set(nums[i], i);
  }
};
