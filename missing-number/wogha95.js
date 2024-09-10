// TC: O(N)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  // result: subN - num의 누적합을 저장하는 변수
  let result = 0;
  // subN: 1부터 N까지 올라가는 변수
  let subN = 1;

  for (const num of nums) {
    result += subN - num;
    subN += 1;
  }

  // 최종 누적합은 (1~N까지 합) - (nums의 모든 원소 합) 이므로 누락된 숫자만 남게 됩니다.
  return result;
};
