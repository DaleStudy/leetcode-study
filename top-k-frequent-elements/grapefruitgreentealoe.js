/**
 * 정수 array nums , 정수 k가 있을때, 가장 빈도가 높은 숫자 k개 리턴. 순서상관 X
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

//nums에 대해서 각 요소에 대해 중복되는 횟수를 구한다. 그리고 내림차순으로 k개 리턴한다.

var topKFrequent = function (nums, k) {
  const numsFreqMap = new Map(); // O(1)

  // O(n) 시간 / O(n) 공간
  for (let i = 0; i < nums.length; i++) {
    const count = (numsFreqMap.get(nums[i]) ?? 0) + 1; // O(1)
    numsFreqMap.set(nums[i], count); // O(1)
  }

  const arrFromFreqMap = [...numsFreqMap]; // O(n) 시간 / O(n) 공간
  arrFromFreqMap.sort((a, b) => b[1] - a[1]); // O(n log n) 시간

  return arrFromFreqMap
    .map((x) => x[0]) // O(n) 시간 / O(n) 공간
    .slice(0, k); // O(k) 시간 / O(k) 공간
};

//O(n) + O(n log n) + O(n) + O(k) = O(n log n)
