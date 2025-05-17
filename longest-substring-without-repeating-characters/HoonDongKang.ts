/**
 * [Problem]: [3] Longest Substring Without Repeating Characters
 * (https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
 */

/*
 * 1. 중복없이 이어는 문자열 중 가장 긴 문자열
 */
function lengthOfLongestSubstring(s: string): number {
    // 시간 복잡도: O(n^2)
    // 공간 복잡도: O(n)
    function bruteForceFunc(s: string): number {
        let max = 0;
        for (let i = 0; i < s.length; i++) {
            const duplicate = new Set<string>();
            let j = i;
            let count = 0;

            while (j < s.length && !duplicate.has(s[j])) {
                duplicate.add(s[j]);
                count++;
                j++;
            }

            max = Math.max(max, count);
        }

        return max;
    }
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function slidingWindowFunc(s: string): number {
        let left = 0;
        let right = 0;
        let window = new Set<string>();
        let max = 0;
        while (right < s.length) {
            if (window.has(s[right])) {
                window.delete(s[left]);
                left++;
            } else {
                window.add(s[right]);
                max = Math.max(max, right - left + 1);
                right++;
            }
            // while (window.has(s[right])) {
            //     window.delete(s[left]);
            //     left++;
            // }

            // window.add(s[right]);
            // max = Math.max(max, right - left + 1);
            // right++;
        }

        return max;
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    //set에서 left 인덱스를 조금 더 빠르게 가져올 수 있음
    function mapFunc(s: string): number {
        let left = 0;
        let max = 0;
        let map = new Map<string, number>();

        for (let right = 0; right < s.length; right++) {
            if (map.has(s[right])) {
                left = Math.max(left, map.get(s[right])! + 1);
            }

            map.set(s[right], right);
            max = Math.max(max, right - left + 1);
        }

        return max;
    }

    return mapFunc(s);
}
