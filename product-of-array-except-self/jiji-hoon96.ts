function productExceptSelf(nums: number[]): number[] {
	const result = new Array(nums.length).fill(1);
	let prefix = 1;
	let suffix = 1;

	for (let i = 0; i < nums.length; i++) {
		result[i] = prefix;
		prefix *= nums[i];
	}

	for (let j = nums.length - 1; j >= 0; j--) {
		result[j] *= suffix;
		suffix *= nums[j];
	}

	return result;
}

productExceptSelf([1, 2, 3, 4]); // [24,12,8,6]
productExceptSelf([-1, 1, 0, -3, 3]); // [0,0,9,0,0]
