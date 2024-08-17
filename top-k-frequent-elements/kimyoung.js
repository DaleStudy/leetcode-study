var topKFrequent = function (nums, k) {
  let obj = {};
  for (const num of nums) {
    obj[num] ? obj[num]++ : (obj[num] = 1);
  }
  let sorted = Object.entries(obj).sort((a, b) => b[1] - a[1]);
  let result = [];
  for (let i = 0; i < k; i++) {
    result.push(sorted[i][0]);
  }
  return result;
};

// test cases
console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2)); // [1, 2]
console.log(topKFrequent([1], 1)); // [1]

// space - O(n) - mapping the object in [key, freq]
// time - O(nlogn) - sorting the mapped objects in the order of frequency
