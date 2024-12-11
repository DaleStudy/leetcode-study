// 정렬을 이용한 풀이
// TC : O(NlogN)
// SC : O(N)

var longestConsecutiveUsingSort = function (nums) {
  if (nums.length === 0) return 0;

  const uniqueNums = [...new Set(nums)].sort((a, b) => a - b);

  let max_cnt = 0;
  let cnt = 1;
  for (let i = 1; i < uniqueNums.length; ++i) {
    if (uniqueNums[i - 1] + 1 == uniqueNums[i]) {
      cnt += 1;
    } else {
      max_cnt = cnt > max_cnt ? cnt : max_cnt;
      cnt = 1;
    }
  }
  max_cnt = cnt > max_cnt ? cnt : max_cnt;
  return max_cnt;
};

// 집합을 이용한 풀이
// TC : O(N)
// SC : O(N)

var longestConsecutive = function (nums) {
  if (nums.length === 0) return 0;
  
  const numSet = new Set(nums);
  let maxLength = 0;
  
  for (const num of numSet) {
      if (!numSet.has(num - 1)) {
          let currentNum = num;
          let currentLength = 1;
          
          while (numSet.has(currentNum + 1)) {
              currentNum++;
              currentLength++;
          }
          
          maxLength = Math.max(maxLength, currentLength);
      }
  }
  
  return maxLength;
};
