/**
 * [Problem]: [56] Merge Intervals
 * (https://leetcode.com/problems/merge-intervals/description/)
 */
function merge(intervals: number[][]): number[][] {
    //시간복잡도 O(n^2)
    //공간복잡도 O(n)
    function bruteForceFunc(intervals: number[][]): number[][] {
        const result: number[][] = [];
        const visited = new Set<number>();

        for (let i = 0; i < intervals.length; i++) {
            if (visited.has(i)) continue;
            visited.add(i);

            while (true) {
                let hasMerged = false;
                for (let j = 0; j < intervals.length; j++) {
                    if (visited.has(j)) continue;

                    const [curA, curB] = intervals[i];
                    const [nextA, nextB] = intervals[j];

                    if (curA <= nextB && nextA <= curB) {
                        visited.add(j);
                        intervals[i] = [Math.min(curA, nextA), Math.max(curB, nextB)];

                        hasMerged = true;
                    }
                }
                if (!hasMerged) break;
            }
            result.push(intervals[i]);
        }
        return result;
    }

    //시간복잡도 O(nlog n)
    //공간복잡도 O(n)
    function sortFunc(intervals: number[][]): number[][] {
        if (!intervals.length) return intervals;
        intervals.sort((a, b) => a[0] - b[0]);

        const result: number[][] = [intervals[0]];
        for (let i = 0; i < intervals.length; i++) {
            const prev = result[result.length - 1];
            const cur = intervals[i];

            if (cur[0] <= prev[1]) {
                prev[1] = Math.max(prev[1], cur[1]);
            } else {
                result.push(cur);
            }
        }

        return result;
    }
}
