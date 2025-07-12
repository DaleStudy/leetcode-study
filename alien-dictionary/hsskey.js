export class Solution {
    /**
     * @param {string[]} words
     * @return {string}
     */
    alienOrder(words) {
        const adj = new Map();
        for (const word of words) {
            for (const char of word) {
                if (!adj.has(char)) {
                    adj.set(char, new Set());
                }
            }
        }

        for (let i = 0; i < words.length - 1; i++) {
            const w1 = words[i];
            const w2 = words[i + 1];
            const minLen = Math.min(w1.length, w2.length);

            if (w1.length > w2.length && w1.slice(0, minLen) === w2.slice(0, minLen)) {
                return "";
            }

            for (let j = 0; j < minLen; j++) {
                if (w1[j] !== w2[j]) {
                    adj.get(w1[j]).add(w2[j]);
                    break;
                }
            }
        }

        const visit = {}; // false: visited, true: current path (cycle detection)
        const res = [];

        const dfs = (c) => {
            if (c in visit) return visit[c];

            visit[c] = true;
            for (const nei of adj.get(c)) {
                if (dfs(nei)) return true;
            }
            visit[c] = false;
            res.push(c);
            return false;
        };

        for (const c of adj.keys()) {
            if (dfs(c)) return "";
        }

        return res.reverse().join('');
    }
}

