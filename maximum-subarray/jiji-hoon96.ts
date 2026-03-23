function maxSubArray(nums: number[]): number {
	let currentSum = nums[0];
	let maxSum = nums[0];

	for (let i = 1; i < nums.length; i++) {
		currentSum = Math.max(currentSum + nums[i], nums[i]);
		maxSum = Math.max(currentSum, maxSum);
	}

	return maxSum;
}

maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]); // 6
maxSubArray([1]); // 1
maxSubArray([5, 4, -1, 7, 8]); // 23
