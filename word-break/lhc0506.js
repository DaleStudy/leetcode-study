/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const wordDictSet = new Set(wordDict);
    const visited = new Set();

    const indexStack = [0];
    while(indexStack.length > 0) {
        const startIndex = indexStack.pop();

        if (visited.has(startIndex)) continue;
        visited.add(startIndex);

        if (startIndex === s.length) return true;

        for (let endIndex = startIndex + 1; endIndex <= s.length; endIndex++) {
            const word = s.substring(startIndex, endIndex);

            if (wordDictSet.has(word)) {
                indexStack.push(endIndex);
            }
        }
    }

    return false;
};
