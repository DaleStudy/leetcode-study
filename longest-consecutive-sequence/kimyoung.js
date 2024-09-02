var longestConsecutive = function (nums) { // sorting approach
    if (!nums.length) return 0;
    let set = new Set(nums);
    let sorted = [...set].sort((a, b) => a - b);
    let longestSeq = 0;
    let currSeq = 1;

    for (let i = 1; i < sorted.length; i++) { // loop through sorted list to find sequence
        if (sorted[i - 1] + 1 === sorted[i]) {
            currSeq++;
        } else {
            longestSeq = Math.max(longestSeq, currSeq); // compare sequence to figure out the longest
            currSeq = 1;
        }
    }
    
    return Math.max(longestSeq, currSeq);
};

// time - O(nlong) using sort
// space - O(n) store nums in set


// TODO - try O(n) TC approach
