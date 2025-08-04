class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = "";

        for (const str of strs) {
            result += `${str.length}#${str}`;
        }

        return result;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(s) {
        let result = [];
        let i = 0;
        // 5#hello5#world
        while (i < s.length) {
            const pos = s.indexOf("#", i);
            const len = parseInt(s.slice(i, pos));// 5
            i = pos + 1;
            const str = s.slice(i, i + len);
            result.push(str);
            i += len;
        }
        return result;
    }
}

