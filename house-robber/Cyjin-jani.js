const rob = function (nums) {
  // 최대 누적값을 저장하는 배열
  const data = [];
  data[0] = nums[0];

  for (let i = 1; i < nums.length; i++) {
    data[i] = Math.max(data[i - 1], (data[i - 2] ?? 0) + nums[i]);
  }

  return data[data.length - 1];
};
