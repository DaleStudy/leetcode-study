/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const counter = new Map();

  nums.forEach((num) => {
    if (counter.has(num)) {
      counter.set(num, counter.get(num) + 1);
    } else {
      counter.set(num, 1);
    }
  });

  const sorted = [...counter.entries()].sort(
    ([, freqA], [, freqB]) => freqB - freqA
  );

  return sorted.slice(0, k).map(([num]) => num);
};

/**
 * Time Complexity: O(n log n)
 * - Counting the frequency of each element takes O(n) time.
 * - Sorting the entries by frequency takes O(n log n) time.
 * - Extracting the top k elements and mapping them takes O(k) time.
 * - Therefore, the overall time complexity is dominated by the sorting step, resulting in O(n log n).

 * Space Complexity: O(n)
 * - The counter map requires O(n) space to store the frequency of each element.
 * - The sorted array also requires O(n) space.
 * - Therefore, the overall space complexity is O(n).
 */
