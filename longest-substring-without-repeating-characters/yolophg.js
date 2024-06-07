// Time Complexity: O(n)
// Space Complexity: O(n)

var lengthOfLongestSubstring = function(s) {
    let charSet = new Set();
    
    let left = 0;
    let right = 0;
    
    let maxLength = 0;
    
    // iterate the string.
    while (right < s.length) {
        if (!charSet.has(s[right])) {
            // if the character isn't in the set, add it.
            charSet.add(s[right]);
            // move the right pointer to the right.
            right++;
            // update the maximum length if the current window is larger.
            maxLength = Math.max(maxLength, right - left);
        } else {
            // if the character is in the set, remove the leftmost character.
            charSet.delete(s[left]);
            // move the left pointer to the right.
            left++;
        }
    }
    
    return maxLength;
};
