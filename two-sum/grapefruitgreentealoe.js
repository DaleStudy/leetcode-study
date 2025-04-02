/**
 * 정수 숫자 배열과 정수 target
 * 숫자 합이 target과 같은 두 숫자의 index를 리턴.
 * 같은 요소 두번 X. 답은 항상 1개
 * 정렬필요 X
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  //순회. target에서 nums[i]를 뺀 요소를 찾기.
  //2중포문. 시간복잡도 O(1)~O(N^2)
  for (let i = 0; i < nums.length; i++) {
    const subNum = target - nums[i]; // 공간 O(1)
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] == subNum) {
        return [i, j];
      }
    }
  }
};
