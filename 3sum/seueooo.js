/**
정렬, 투포인터
정렬 후, 첫 번째 수를 고정하고 나머지 두 수를 투포인터로 탐색
중복되는 경우는 스킵
시간 복잡도: O(n^2)
공간 복잡도: O(n)
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  let n = nums.length;
  let answer = [];
  for (let i = 0; i < n - 2; i++) {
    let l = i + 1;
    let h = n - 1;
    if (nums[i] > 0) break;
    // 중복 제거
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    while (l < h) {
      const sum = nums[i] + nums[l] + nums[h];
      if (sum > 0) {
        h--;
      } else if (sum < 0) {
        l++;
      } else {
        answer.push([nums[i], nums[l], nums[h]]);
        while (l < h && nums[l] === nums[l + 1]) l++;
        while (l < h && nums[h] === nums[h - 1]) h--;
        l++;
        h--;
      }
    }
  }
  return answer;
};
