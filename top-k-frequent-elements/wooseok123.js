// TC : o(n log n) | SC : o(n)

var topKFrequent = function (nums, k) {
  const elements = countElments(nums);
  const keys = Object.keys(elements).sort((a, b) => elements[b] - elements[a]);
  return keys.slice(0, k);
};

let countElments = (nums) => {
  const temp = {};
  for (const num of nums) {
    temp[num] = (count[num] || 0) + 1;
  }
  return temp;
};
