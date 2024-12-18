/**
 * @param {number[]} nums
 * @return {number[][]}
 */


// Time Complexity: O(n^2)
// Space Complexity: O(n^2)

var threeSum = function (nums) {

    const sorted = [...nums].sort((a, b) => a - b);

    let result = [];

    // Loop through the array and pick each number as the first number for the triplet
    for (let i = 0; i < sorted.length - 2; i++) {

        // skip duplicate values for sorted[middle]
        if(i > 0 && sorted[i - 1] === sorted[i]) {
            continue;
        }

        let left = i + 1; // Left pointer starts right after the current middle
        let right = sorted.length - 1; // Right pointer starts at the last element

        while (left < right) {
            const sum = sorted[i] + sorted[left] + sorted[right];

            if (sum === 0) {
                result.push([sorted[left], sorted[i], sorted[right]]);

                // skip duplicates for sorted[left] and sorted[right]
                while(left < right && sorted[left] === sorted[left + 1]){
                    left += 1; // Move left pointer to the right to skip duplicate values
                } 

                while(left < right && sorted[right] === sorted[right - 1]) {
                    right -= 1; // Move right pointer to the left to skip duplicate values
                }

                left += 1; 
                right -= 1;

            } else if (sum > 0) {
                right -= 1;

            } else {
                left += 1
            }
        }
    }

     return result;
  
};


// var threeSum = function (nums) {

// i != j, i != k, and j != k can be interpreted as i < j < k

    // three nested loops
    // time complexity of O(n³)
    // Time Limit Exceeded

    // let result = [];

    // for (let i = 0; i < nums.length - 2; i++) {
    //     for (let j = i + 1; j < nums.length - 1; j++) {
    //         for (let k = j + 1; k < nums.length; k++) {
    //             if (nums[i] + nums[j] + nums[k] === 0) {
    //                 const str = [nums[i], nums[j], nums[k]].sort((a, b) => a - b).join(",")
    //                 result.push(str)
    //             }
    //         }
    //     }

    // }

    // result = [... new Set(result)].map(str => str.split(",").map(str => +str))

    // return result;
    
// }

