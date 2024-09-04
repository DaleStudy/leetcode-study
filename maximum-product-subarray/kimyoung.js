var maxProduct = function (nums) { // brute force approach
    let subarrays = [];
    for (let i = 0; i < nums.length; i++) { // get subarrays
        for (let j = i; j < nums.length; j++) {
            subarrays.push(nums.slice(i, j + 1));
        }
    }

    let maxProduct = 0;
    subarrays.forEach(arr => { // find product of each subarray and compare to maxProduct
        let prod = arr.reduce((acc, el) => acc *= el, 1);
        max = Math.max(prod, max);
    })

    return maxProduct;
};

// time - O(n^2) double for loop
// space - O(n^2) total count of subarrays = n*(n+1)/2



// TODO - different approach
