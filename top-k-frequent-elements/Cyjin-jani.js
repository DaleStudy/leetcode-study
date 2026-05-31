const topKFrequent = function (nums, k) {
  const tempArr = Array.from({ length: nums.length }, () => []);
  const obj = {};

  for (let num of nums) {
    obj[num] = (obj[num] || 0) + 1;
  }

  for (let key in obj) {
    const val = obj[key] - 1;
    tempArr[val].push(+key);
  }

  // answer.flat(), return answer.slice(-k) 대신 좀 더 최적화된 코드로 변경합니다.
  const answer = [];
  for (let i = tempArr.length - 1; i >= 0; i--) {
    for (let num of tempArr[i]) {
      answer.push(num);
      if (answer.length === k) return answer;
    }
  }
  return answer;
};
