/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
const merge = function (intervals) {
    // 시작점 기준으로 정렬
    intervals.sort((a, b) => Number(a[0]) - Number(b[0]));
    const result = [];

    for (const current of intervals) {
        const last = result[result.length - 1];

        // 겹치는 구간이 있으면, 구간의 끝점을 더 큰 것으로 덮어씌우기
        if (last && current[0] <= last[1]) {
            result[result.length - 1][1] = Math.max(current[1], last[1]);
        }
        // 겹치는 구간이 없으면, 새로 집어 넣기
        else {
            result.push(current);
        }
    }

    return result;
};

// 시간복잡도: O(n * log n)
// 공간복잡도: O(n)
