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
  const array = [];
  const hashTable = new Map();

  nums.forEach((num) => hashTable.set(num, (hashTable.get(num) ?? 0) + 1));

  hashTable.forEach((count, number) => array.push({ number, count }));

  array.sort((a, b) => b.count - a.count);

  for (let i = 0; i < k; i++) answer.push(array[i].number);

  return answer;
};
