/**
 * [Problem]: [76] Minimum Window Substring
 * (https://leetcode.com/problems/minimum-window-substring/description/)
 */
function minWindow(s: string, t: string): string {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function windowFunc(s: string, t: string): string {
        let left = 0;
        let right = 0;
        let s_map = new Map<string, number>();
        let t_map = new Map<string, number>();
        let minCount = Infinity;
        let minStart = 0;

        for (const char of t) {
            t_map.set(char, (t_map.get(char) || 0) + 1);
        }

        while (right < s.length) {
            let char = s[right];
            s_map.set(char, (s_map.get(char) || 0) + 1);
            right++;

            while (isValid(s_map)) {
                if (right - left < minCount) {
                    minCount = right - left;
                    minStart = left;
                }

                let char = s[left];
                s_map.set(char, s_map.get(char)! - 1);
                left++;
            }
        }

        return minCount === Infinity ? "" : s.slice(minStart, minStart + minCount);

        function isValid(map: Map<string, number>): boolean {
            for (let i of t_map.keys()) {
                if ((map.get(i) || 0) < t_map.get(i)!) return false;
            }
            return true;
        }
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function optimizedFunc(s: string, t: string): string {
        const map = new Map<string, number>();
        let required = t.length;
        let left = 0;
        let minLen = Infinity;
        let minStart = 0;

        for (const char of t) {
            map.set(char, (map.get(char) || 0) + 1);
        }

        for (let right = 0; right < s.length; right++) {
            const char = s[right];

            if (map.has(char)) {
                const count = map.get(char)!;
                if (0 < count) required--;
                map.set(char, count - 1);
            }

            while (required === 0) {
                const char = s[left];

                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }

                if (map.has(char)) {
                    map.set(char, map.get(char)! + 1);
                    if (map.get(char)! > 0) {
                        required++;
                    }
                }
                left++;
            }
        }
        return minLen === Infinity ? "" : s.slice(minStart, minStart + minLen);
    }
}
