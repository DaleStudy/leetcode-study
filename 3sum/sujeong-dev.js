/**
 * @param {number[]} nums
 * @return {number[][]}
 * 
 * 시간복잡도: 이중 for문으로 O(n^2)이긴한데 너무 오래걸림
 * 해설 확인해보기
 */
var threeSum = function (nums) {
  if (nums.every((num) => num === 0)) return [nums.slice(0, 3)];

  const threeSet = new Set();
  for (let i = 0; i < nums.length - 2; i++) {
    const twoSet = new Set();
    for (let j = i + 1; j < nums.length; j++) {
      const findNum = -(nums[i] + nums[j]);
      if (twoSet.has(findNum)) {
        const triplet = [nums[i], nums[j], findNum].sort((a, b) => a - b);
        threeSet.add(triplet.join(','));
      }
      twoSet.add(nums[j]);
    }
  }
  return Array.from(threeSet, (k) => k.split(',').map(Number));
};
