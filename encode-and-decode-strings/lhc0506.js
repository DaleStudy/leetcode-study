class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return JSON.stringify(strs);
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        return JSON.parse(str);
    }
}
