/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
	if( nums.length < 1 ) { return nums[0]}

	let prev_2 = nums[0]
	let prev_1 = Math.max(nums[0], nums[1]);

	for( let i= 2; i <nums.length; i++ ) {
		let crr = Math.max(prev_1, nums[i]+ prev_2 );
		prev_2 = prev_1;
		prev_1  = crr;
	}

	return prev_1;
};
/* 
TC: O(n)
SC: O(1)
*/


/* Test Case */
console.log(rob([1,2,3,1]));
console.log(rob([2,7,9,3,1]));


