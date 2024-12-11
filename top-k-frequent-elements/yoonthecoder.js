var topKFrequent = function (nums, k) {
  // 1. count the frequency of each number in the array
  const map = new Map();

  // iterating through the array to count how many times each num appears.
  for (const num of nums) {
    // if the num already exists in the map, increment its count
    if (map.has(num)) {
      map.set(num, map.get(num) + 1);
    } // otherwise, set it to 1
    else map.set(num, 1);
  }

  // 2.create an array to store the freqeuncy numbers
  const freqArr = [];
  for (const [num, freq] of map) {
    freqArr.push([num, freq]);
  }
  // sort in descending order by frequency
  freqArr.sort((a, b) => b[1] - a[1]);
  return freqArr.slice(0, k).map(([num]) => num);
};

// Time complexity: O(nlogn)
// Space complexity: O(n)
