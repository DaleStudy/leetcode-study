/**
map을 사용해서 구하려고 하는 값(인덱스)을 value로 둔다. → {value: index} 역전
map에 {value: index}를 반복하여 저장한다.
in 연산자로 find_num이 map의 key와 일치하는지 비교한다.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  let map = {};
  let find_num = 0;

  for (let i = 0; i < nums.length; i++) {
    find_num = target - nums[i];

    if (find_num in map) {
      return [map[find_num], i];
    }

    map[nums[i]] = i;
  }
}
