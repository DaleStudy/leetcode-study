// Approach 2: binary search
// Time Complexity: ✅ O(log n)
// Space Complexity: O(1)

function findMin(nums: number[]): number {

    let left = 0
    let right = nums.length - 1

    while(left < right) {

        const mid = Math.floor((left + right) / 2)

        if(nums[mid] > nums[right]) {
            // the min must be to the right of mid
            left = mid + 1
        } else {
            // the mins could be mid or to the left
            right = mid
        }
    }

    return nums[left]  
};


// Approach 1:
// Time Complexity: ❌ O(n)
// Space Complexity: O(1)

// function findMin(nums: number[]): number {
//   // input: an array of length n sorted in ascending order
//   // rotate: a[n-1], a[0], ..., a[n-2]
//   // time complexity allowed: O(log n)

//   let first = nums[0];
//   let last = nums[nums.length - 1];
//   let cnt = 0;

//   while (first > last) {
//     first = last;
//     cnt += 1;
//     last = nums[nums.length - 1 - cnt];
//   }

//   return first;
// }

