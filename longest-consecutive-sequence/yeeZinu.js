/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  // set으로 중복된 element 제거
  const numSet = new Set(nums);
  // 최대 연속 길이 변수
  let maxLength = 0;

  // 최대 연속 길이 찾기
  for (let num of numSet) {
    // 만약 현재 수 -1이 없다면?
    if (!numSet.has(num - 1)) {
      let currentNum = num;   //현재값이 시작
      let currentLength = 1;  //최대 길이 1로 초기화

      // 현재값 +1이 있을 때 까지 반복
      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentLength++;
      }

      // 최대길이 값과 현재 길이값중 더 높은것이 최대길이값
      maxLength = Math.max(maxLength, currentLength);
    }
  }
  return maxLength;
};
