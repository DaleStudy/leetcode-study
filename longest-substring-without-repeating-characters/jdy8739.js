/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0;
    let end = 0;

    const set = new Set();

    let max = 0;

    while (end < s.length) {
        const char = s[end];

        if (set.has(char)) {
            set.delete(s[start]);

            start++;
        } else {
            set.add(char);

            end++;
        }

        max = Math.max(max, set.size);
    }

    return max;
};

//
//



