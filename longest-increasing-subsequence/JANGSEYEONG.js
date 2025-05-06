/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
  let sub = [nums[0]]; // 가장 첫번째 원소 일단 넣고 보기
  for (const num of nums.slice(1)) {
    if (num > sub[sub.length - 1]) {
      // 수열의 마지막값보다 크면 무조건 추가
      sub.push(num);
    } else {
      // 수열의 마지막값보다 작다면 이 숫자보다 큰 숫자들 중 가장 작은 숫자를 찾아서 교체
      let i = 0;
      while (sub[i] < num) {
        i++;
      }
      sub[i] = num;
    }
  }
  return sub.length;
};
