// Time Complexity: O(n)
// Space Complexity: O(1)

var characterReplacement = function(s, k) {
    let maxLen = 0; 
    // initialize an array to store the count of each character.
    let charCounts = new Array(26).fill(0); 
    let start = 0;

    // iterate the string with the end pointer.
    for (let end = 0; end < s.length; end++) {
        // calculate the index of the character.
        let charIndex = s.charCodeAt(end) - 65; 
        // update maxCount with the maximum count.
        maxLen = Math.max(maxLen, ++charCounts[charIndex]); 

        // move the start pointer and decrement the count at that position.
        if (end - start + 1 - maxLen > k) {
            charCounts[s.charCodeAt(start) - 65]--;
            start++;
        }
    }

    return s.length - start;
};
