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

  const answer = tempArr.flat();
  return answer.slice(-k);
};
