// Time Complexity: O(n), O(n)
// Space Complexity: O(n), O(n)

class Solution {
    encode(strs) {
        // join the array into a single string using a delimiter, '|'.
        return strs.join('|');
    }

    decode(str) {
        // split the string using the delimiter '|' and return the array.
        return str.split('|');
    }
}
