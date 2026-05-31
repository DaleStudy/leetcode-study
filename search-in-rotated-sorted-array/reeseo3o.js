const searchRotated = (nums, target) => {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) return mid;

        const isLeftSorted = nums[left] <= nums[mid];

        if (isLeftSorted) {
            const inLeft =
                nums[left] <= target && target < nums[mid];
            if (inLeft) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            const inRight =
                nums[mid] < target && target <= nums[right];
            if (inRight) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
};
