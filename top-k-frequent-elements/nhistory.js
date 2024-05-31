var topKFrequent = function (nums, k) {
  // 1. Hashmap { num : frequency }
  let map = {};

  // 2. Iterate counts frequency of each value
  for (num of nums) {
    // Check there is already num key or not
    if (!map[num]) map[num] = 0;
    map[num]++;
  }

  // 3. Sort frequency and return sliced array
  return [...Object.keys(map)].sort((a, b) => map[b] - map[a]).slice(0, k);
};
