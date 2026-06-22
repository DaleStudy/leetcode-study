var longestConsecutive = function (nums) {
  // 숫자 존재 유무를 확인할 수 있는 자료구조 세팅
  const dataSet = new Set(nums);
  let answer = 0;

  // 전체 숫자를 순회하면서 시작점을 확인
  for (let num of dataSet) {
    // num - 1이 dataSet에 있는지 확인. 있다면 시작점이 아니므로 패스
    if (!dataSet.has(num - 1)) {
      // 없다면 시작점. 여기서부터 연속된 숫자가 얼마나 있는지 카운팅.
      let count = 1;
      let target = num;
      while (dataSet.has(target + 1)) {
        count++;
        target++;
      }
      // longest를 구하는 문제이므로 max로 더 긴 답을 판단
      answer = Math.max(count, answer);
    }
  }
  return answer;
};
