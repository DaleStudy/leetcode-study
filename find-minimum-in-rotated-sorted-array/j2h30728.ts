function findMin(nums: number[]): number {
    const n = nums.length - 1;
    let last = nums[n];
    let left = 0, right = n;
    
    while(left < right){
        const mid = (left + right) >> 1;
        if(nums[mid] > last) left = mid + 1;
        else right = mid;
    }
    return nums[left];
};
