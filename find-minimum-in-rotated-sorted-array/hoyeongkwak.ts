function findMin(nums: number[]): number {
    /*
    space complexity: 1
    time complexity : nlogn
    */
    // return nums.sort((a, b) => a - b)[0]

    /*
    space complexity: 1
    time complexity : logn
    */
    let left = 0
    let right = nums.length - 1

    while (left < right) {
        const mid = left + Math.floor((right - left) / 2)
        if (nums[mid] > nums[right]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return nums[left]
};
