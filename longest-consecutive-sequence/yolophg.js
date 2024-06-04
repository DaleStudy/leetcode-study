// Time Complexity: O(n log n)
// Space Complexity: O(n)

var longestConsecutive =  function(nums) {
    if (nums.length === 0) return 0;

    nums.sort((a, b) => a - b);

    let longestStreak = 1;
    let currentStreak = 1;

    // iterate through the sorted array.
    for (let i = 1; i < nums.length; i++) {
        // check for duplicates.
        if (nums[i] !== nums[i - 1]) { 
            if (nums[i] === nums[i - 1] + 1) {
                // if current element is consecutive, increment current streak.
                currentStreak++;
            } else {
                // if not, update longest streak and reset current streak.
                longestStreak = Math.max(longestStreak, currentStreak);
                currentStreak = 1;
            }
        }
    }

    // final comparison to ensure the longest streak is captured.
    longestStreak = Math.max(longestStreak, currentStreak);

    return longestStreak;
}
