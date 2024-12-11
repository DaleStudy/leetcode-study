// 풀이
// Set으로 중복 제거 후 nums와 길이 비교

// TC : O(N)
// SC : O(N)

var containsDuplicate = function(nums) {
  return new Set(nums).size !== nums.length
};

