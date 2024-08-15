/**
 * @description
 * time complexity: O(N logN)
 * space complexity: O(N)
 *
 * brainstorming:
 * 1. javascript sort method
 * 2. priority queue
 *
 * strategy:
 * javascript sort method
 *
 * reason:
 * javascript sort method is easier to implement.
 */

var topKFrequent = function (nums, k) {
  const answer = [];
  const hashTable = new Map();

  nums.forEach((num) => hashTable.set(num, (hashTable.get(num) ?? 0) + 1));

  hashTable.forEach((count, number) => answer.push({ number, count }));

  return answer
    .sort((a, b) => b.count - a.count)
    .slice(0, k)
    .map(({ number }) => number);
};
